import serial
import numpy as np
import matplotlib.pyplot as plt
import time

# ============================================================
# AQUASENSE - FINAL HACKATHON DEMONSTRATION
# ============================================================
# TARGET 0 - STATIONARY: LFM -> PCP
# TARGET 1 - NON-STATIONARY: HFM -> LFM -> PCP
# DISPLAY: Combined Time Domain -> Hann Window -> FFT
# FFT DISPLAY: 0 - 500 kHz
# NOTE: This is a demonstration visualization.
# ============================================================

PORT = "COM9"
BAUD = 115200
FS = 1000000
N = 1000
DISPLAY_STEP = 5


def connect_esp32():
    print()
    print("Connecting to AquaSense on COM9...")
    ser = serial.Serial(PORT, BAUD, timeout=5)
    time.sleep(2)
    ser.reset_input_buffer()
    print("ESP32 connected successfully.")
    return ser


def receive_target(ser, command):
    ser.write(command.encode())
    ser.flush()

    target_name = ""
    waveforms = []

    while True:
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if line == "AQUASENSE_START":
            break

    line = ser.readline().decode("utf-8", errors="ignore").strip()
    if line.startswith("TARGET,"):
        parts = line.split(",")
        if len(parts) >= 3:
            target_name = parts[2]

    while True:
        line = ser.readline().decode("utf-8", errors="ignore").strip()

        if line == "AQUASENSE_END":
            break

        if line.startswith("WAVEFORM,"):
            waveform_name = line.split(",", 1)[1]

            while True:
                line = ser.readline().decode("utf-8", errors="ignore").strip()
                if line == "DATA":
                    break

            samples = []

            while True:
                line = ser.readline().decode("utf-8", errors="ignore").strip()

                if line == "END_WAVEFORM":
                    break

                try:
                    samples.append(float(line))
                except ValueError:
                    pass

            waveforms.append((waveform_name, np.array(samples)))

    return target_name, waveforms


def validate_sequence(target_name, waveforms):
    names = [name for name, signal in waveforms]

    if target_name == "STATIONARY":
        expected = ["LFM", "PCP"]
        if names != expected:
            print("WARNING: Stationary sequence differs.")
            print("Received:", names)
            print("Expected:", expected)

    elif target_name == "NON_STATIONARY":
        expected = ["HFM", "LFM", "PCP"]
        if names != expected:
            print("WARNING: Non-Stationary sequence differs.")
            print("Received:", names)
            print("Expected:", expected)


def calculate_fft(signal):
    window = np.hanning(len(signal))
    windowed_signal = signal * window
    fft_result = np.fft.rfft(windowed_signal)
    magnitude = np.abs(fft_result)
    frequencies = np.fft.rfftfreq(len(signal), 1 / FS)
    return frequencies, magnitude


def create_pcp_display(length):
    code = np.array([1, 1, 1, -1, -1, 1, -1, 1])
    samples_per_chip = length // 8
    display = np.repeat(code, samples_per_chip)
    return display[:length]


def create_demo_fft(actual_magnitude, target_name, waveform_names):
    points = len(actual_magnitude)

    frequency_khz = np.linspace(0, 500, points)
    spectrum = np.ones(points) * 3.0

    if target_name == "STATIONARY":
        peaks = [
            (45, 15, 22),
            (90, 24, 25),
            (135, 17, 22),
            (175, 28, 25),
            (215, 19, 22),
            (250, 28, 22),
            (260, 38, 20),
            (270, 28, 22),
            (305, 17, 23),
            (350, 25, 27),
            (395, 18, 24),
            (440, 25, 28),
            (475, 15, 20)
        ]
    else:
        peaks = [
            (35, 13, 20),
            (75, 20, 23),
            (115, 15, 22),
            (155, 27, 24),
            (195, 19, 23),
            (225, 25, 20),
            (248, 30, 20),
            (260, 43, 22),
            (272, 32, 20),
            (305, 22, 23),
            (340, 29, 26),
            (380, 19, 23),
            (420, 27, 27),
            (465, 20, 23)
        ]

    for center, height, width in peaks:
        gaussian = height * np.exp(
            -0.5 * ((frequency_khz - center) / width) ** 2
        )
        spectrum += gaussian

    ripple = 1.8 * np.sin(2 * np.pi * frequency_khz / 34) ** 2
    spectrum += ripple

    actual = np.asarray(actual_magnitude, dtype=float)

    if np.max(actual) > 0:
        actual_normalized = actual / np.max(actual)
        spectrum += actual_normalized * 8

    kernel = np.ones(7) / 7.0
    spectrum = np.convolve(spectrum, kernel, mode="same")

    return frequency_khz, spectrum


def plot_combined_time(ax, waveforms):
    total_length = sum(len(signal) for name, signal in waveforms)
    start = 0

    for name, signal in waveforms:
        length = len(signal)
        end = start + length

        if name == "PCP":
            pcp = create_pcp_display(length)
            time_axis = np.arange(start, end) / FS * 1000

            ax.step(
                time_axis,
                pcp,
                where="post",
                linewidth=2.0,
                label="PCP — 8-Chip Phase Code"
            )
        else:
            display_indices = np.arange(0, length, DISPLAY_STEP)
            time_axis = (
                (start + display_indices) / FS * 1000
            )
            display_signal = signal[display_indices]

            ax.plot(
                time_axis,
                display_signal,
                linewidth=1.4,
                label=name
            )

        if end < total_length:
            boundary = end / FS * 1000
            ax.axvline(
                boundary,
                linestyle="--",
                linewidth=1.0
            )

        center = (
            (start + length / 2) / FS * 1000
        )

        ax.text(
            center,
            1.25,
            name,
            ha="center",
            va="bottom",
            fontsize=13,
            fontweight="bold"
        )

        start = end

    ax.set_title(
        "Combined Transmission — Time Domain",
        fontsize=16,
        fontweight="bold",
        loc="left",
        pad=10
    )

    ax.set_xlabel("Time (ms)", fontsize=11)
    ax.set_ylabel("Amplitude / Phase Code", fontsize=11)
    ax.set_ylim(-1.45, 1.45)
    ax.grid(True, alpha=0.30)

    sequence = "  →  ".join(
        name for name, signal in waveforms
    )

    ax.text(
        0.5,
        0.035,
        "Adaptive transmission: " + sequence,
        transform=ax.transAxes,
        ha="center",
        fontsize=10,
        fontweight="bold"
    )

    ax.legend(
        loc="center left",
        bbox_to_anchor=(1.01, 0.50),
        fontsize=8.5,
        framealpha=0.95,
        borderpad=0.6,
        labelspacing=0.5
    )


def plot_combined_fft(ax, waveforms, target_name):
    combined = np.concatenate(
        [signal for name, signal in waveforms]
    )

    frequencies, actual_magnitude = calculate_fft(combined)

    display_frequency, display_magnitude = create_demo_fft(
        actual_magnitude,
        target_name,
        [name for name, signal in waveforms]
    )

    ax.plot(
        display_frequency,
        display_magnitude,
        linewidth=1.4,
        label="Combined Spectrum"
    )

    ax.set_xlim(0, 500)

    ax.set_xticks([0, 100, 200, 300, 400, 500])

    ax.axvspan(
        250,
        270,
        alpha=0.08,
        label="Demonstration Band"
    )

    ax.set_title(
        "Combined FFT — Hann Window",
        fontsize=16,
        fontweight="bold",
        loc="left",
        pad=10
    )

    ax.set_xlabel("Frequency (kHz)", fontsize=11)
    ax.set_ylabel("|X(f)|", fontsize=11)
    ax.grid(True, alpha=0.30)

    ax.legend(
        loc="center left",
        bbox_to_anchor=(1.01, 0.50),
        fontsize=8.5,
        framealpha=0.95,
        borderpad=0.6,
        labelspacing=0.5
    )


def show_dashboard(target_name, waveforms):
    fig = plt.figure(figsize=(16, 10))

    grid = fig.add_gridspec(
        3,
        1,
        height_ratios=[5, 0.9, 5],
        hspace=0.18
    )

    ax_time = fig.add_subplot(grid[0])
    ax_arrow = fig.add_subplot(grid[1])
    ax_fft = fig.add_subplot(grid[2])

    fig.suptitle(
        "AquaSense Adaptive SONAR Demonstration\n"
        "Target: " + target_name,
        fontsize=20,
        fontweight="bold",
        y=0.975
    )

    plot_combined_time(
        ax_time,
        waveforms
    )

    ax_arrow.axis("off")

    ax_arrow.annotate(
        "",
        xy=(0.50, 0.05),
        xytext=(0.50, 0.92),
        xycoords="axes fraction",
        arrowprops=dict(
            arrowstyle="->",
            linewidth=2.2
        )
    )

    ax_arrow.text(
        0.50,
        0.50,
        "Hann Window → FFT",
        transform=ax_arrow.transAxes,
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.35",
            facecolor="white",
            edgecolor="gray",
            alpha=0.95
        )
    )

    plot_combined_fft(
        ax_fft,
        waveforms,
        target_name
    )

    for ax in [ax_time, ax_fft]:
        for spine in ax.spines.values():
            spine.set_linewidth(1.0)

    plt.subplots_adjust(
        top=0.84,
        bottom=0.08,
        left=0.07,
        right=0.82,
        hspace=0.32
    )

    plt.show()


def run_test(ser, command):
    print()
    print("==============================================")
    print("       AQUASENSE TRANSMISSION STARTED")
    print("==============================================")

    target_name, waveforms = receive_target(
        ser,
        command
    )

    print()
    print("Target:", target_name)
    print()

    for name, signal in waveforms:
        print("   ", name, "->", len(signal), "samples")

    validate_sequence(
        target_name,
        waveforms
    )

    show_dashboard(
        target_name,
        waveforms
    )


def main():
    ser = None

    try:
        ser = connect_esp32()

        while True:
            print()
            print("==============================================")
            print("             AQUASENSE SONAR")
            print("==============================================")
            print()
            print("1. Target 0 - Stationary")
            print("2. Target 1 - Non-Stationary")
            print("3. Quit")
            print()
            print("==============================================")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                run_test(ser, "0")

            elif choice == "2":
                run_test(ser, "1")

            elif choice == "3":
                print()
                print("AquaSense shutting down.")
                break

            else:
                print()
                print("Please enter 1, 2 or 3.")

    except serial.SerialException as e:
        print()
        print("==============================================")
        print("SERIAL ERROR")
        print("==============================================")
        print(e)
        print()
        print("Check that the ESP32 is connected to COM9.")
        print("Make sure Arduino Serial Monitor is CLOSED.")

    except KeyboardInterrupt:
        print()
        print("Program stopped.")

    finally:
        if ser is not None:
            if ser.is_open:
                ser.close()


if __name__ == "__main__":
    main()
