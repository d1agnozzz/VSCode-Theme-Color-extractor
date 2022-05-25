import re


def extract_colors(filename: str) -> set[str]:
    """Returns set of all HEX colors from given filename"""
    with open(filename, "r") as f:

        text = f.read()

        # regex matches every HEX code in lines not starting with '//' (not commented lines)
        regex = r"^(?!\s*//)(?:.*)(#([A-Za-z0-9]{6})).*$" 

        p = re.compile(regex, re.MULTILINE)
        m = re.finditer(p, text)

        captured_colors = set()

        for x in m:
            captured_colors.add(x.group(1).upper())
        return captured_colors


if __name__ == "__main__":
    colors = extract_colors("theme_colors.jsonc")
    print(len(colors))
    print(sorted(colors))


"""['#000000', '#161613', '#1D1E19', '#272822', '#3B3C35', '#57584F', '#66D9EF', '#6796E6', '#6E7066', '#919288', '#A6E22E', '#AE81FF', '#B267E6', '#C0C1B5', '#CD9731', '#E6DB74', '#F44747', '#F92672', '#FD971F', '#FDFFF1', '#FFFFFF']"""
