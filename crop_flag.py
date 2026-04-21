#!/usr/bin/env python3
import sys
from pathlib import Path
from PIL import Image, ImageEnhance


def main() -> None:
    if len(sys.argv) not in (2, 3):
        print(f"usage: {Path(sys.argv[0]).name} <decoded_image.png> [output.png]")
        raise SystemExit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) == 3 else Path("flag_crop.png")

    img = Image.open(input_path).convert("RGB")
    w, h = img.size

    # bottom text line where the flag appears in the decoded SSTV frame
    crop = img.crop((int(w * 0.06), int(h * 0.86), int(w * 0.94), int(h * 0.99)))
    crop = crop.resize((crop.width * 6, crop.height * 6), Image.Resampling.LANCZOS)
    crop = ImageEnhance.Contrast(crop).enhance(1.8)
    crop = ImageEnhance.Sharpness(crop).enhance(2.2)
    crop.save(output_path)
    print(f"[+] wrote {output_path}")


if __name__ == "__main__":
    main()
