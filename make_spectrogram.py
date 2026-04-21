#!/usr/bin/env python3
import sys
from pathlib import Path
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt


def main() -> None:
    if len(sys.argv) not in (2, 3):
        print(f"usage: {Path(sys.argv[0]).name} <input.wav> [output.png]")
        raise SystemExit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) == 3 else Path("spectrogram.png")

    rate, data = wav.read(input_path)
    if getattr(data, "ndim", 1) > 1:
        data = data.mean(axis=1)

    plt.figure(figsize=(16, 6))
    plt.specgram(data, NFFT=2048, Fs=rate, noverlap=1536)
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.title(f"Spectrogram: {input_path.name}")
    plt.ylim(0, 4000)
    plt.tight_layout()
    plt.savefig(output_path, dpi=180)
    print(f"[+] wrote {output_path}")


if __name__ == "__main__":
    main()
