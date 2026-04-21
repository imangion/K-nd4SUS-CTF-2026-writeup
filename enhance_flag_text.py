#!/usr/bin/env python3
import sys
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter


def main() -> None:
    if len(sys.argv) not in (2, 3):
        print(f"usage: {Path(sys.argv[0]).name} <flag_crop.png> [output.png]")
        raise SystemExit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) == 3 else Path("flag_text_zoom.png")

    img = Image.open(input_path).convert("RGB")
    img = img.resize((img.width * 2, img.height * 2), Image.Resampling.LANCZOS)
    img = ImageEnhance.Contrast(img).enhance(2.4)
    img = ImageEnhance.Sharpness(img).enhance(3.0)
    img = img.filter(ImageFilter.UnsharpMask(radius=1.4, percent=180, threshold=2))
    img.save(output_path)
    print(f"[+] wrote {output_path}")


if __name__ == "__main__":
    main()
