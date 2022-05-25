from HEX_extractor import extract_colors
import argparse
import os

# Usage:   python create_ACT.py <theme_colors> <out_file>
# Example: python create_ACT.py theme_colors.jsonc palette.act

def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")[:6]
    size = len(value)
    return tuple(int(value[i : i + 2], 16) for i in range(0, size, 2))


def write_ACT(HEX_colors: set[str], filename: str):
    """Save given HEX colors as ACT file"""

    HEX_colors = sorted(HEX_colors)

    bytes = bytearray(768)

    for i, hex_color in enumerate(HEX_colors):
        for j, component in enumerate(hex_to_rgb(hex_color)):
            bytes[(i * 3) + j] = component

    if filename.find('/') != -1:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
    with open(filename, "wb+") as act:
        act.write(bytes)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("colors", help="path to a file with theme colors", type=str)
    parser.add_argument("filename", help="path to output ACT file", type=str)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    HEX_colors = extract_colors(args.colors)
    write_ACT(HEX_colors, args.filename)
