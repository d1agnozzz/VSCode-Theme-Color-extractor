from HEX_extractor import extract_colors
from PIL import Image, ImageColor
import argparse

# Usage:   python create_palette_image.py <theme_colors> <out_image>
# Example: python create_palette_image.py theme_colors.jsonc palette.png


def save_palette_PNG(HEX_colors: set[str], save_path: str):
    """Save given HEX colors as a single row PNG"""

    palette_img = Image.new(
        "RGBA", (len(HEX_colors), 1), ImageColor.getrgb("#00000000")
    )

    HEX_colors = sorted(HEX_colors)

    pixels = palette_img.load()

    for i in range(len(HEX_colors)):
        color = ImageColor.getrgb(HEX_colors.pop())
        color = (*color, 255) if len(color) == 3 else color
        pixels[i, 0] = color

    palette_img.save(save_path, "PNG")


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("colors", help="path to a file with theme colors", type=str)
    parser.add_argument("image", help="path to output PNG image", type=str)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_opt()
    HEX_colors = extract_colors(args.colors)
    save_palette_PNG(HEX_colors, args.image)
