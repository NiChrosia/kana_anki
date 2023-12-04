from PIL import Image
from argparse import ArgumentParser

START_X = 131
START_Y = 133

TILE_WIDTH = 161
TILE_HEIGHT = 154

KATA_OFFSET = TILE_WIDTH + 1

HORIZ_OFFSET = 340
VERT_OFFSET = 234

VOWELS = list("aiueo")
CONSONANTS = list("_kstnhmyrwn")

all_kana: Image.Image | None = None

def find_kana(c: str, v: str, katakana: bool) -> tuple[int, int]:
    if v == "_":
        v = "a"

    c_index = CONSONANTS.index(c)
    v_index = VOWELS.index(v)

    x = START_X + HORIZ_OFFSET * v_index
    y = START_Y + VERT_OFFSET * c_index

    if katakana:
        x += KATA_OFFSET

    return (x, y)

def save_kana(c: str, v: str, katakana: bool, filename: str):
    """c is any valid lowercase Japanese consonant or _ if no
    consonant, and v is any one of aiueo, or _ if no vowel"""

    global all_kana

    if not all_kana:
        all_kana = Image.open("kana.png")

    x, y = find_kana(c, v, katakana)

    kana = all_kana.copy().crop((x, y, x + TILE_WIDTH - 1, y + TILE_HEIGHT - 1))
    kana.save(filename)

def main():
    parser = ArgumentParser(prog="save_kana", description="saves the stroke order for a specified kana")
    parser.add_argument("consonant", help="the lowercase character of the consonant, or _ for no consonant")
    parser.add_argument("vowel", help="the vowel of the kana (aiueo), or _ for no vowel")
    parser.add_argument("-k", "--katakana", action="store_true", help="whether to use katakana, or hiragana if absent")

    args = parser.parse_args()

    c = args.consonant
    v = args.vowel
    k = args.katakana

    filename = c + v + ("_kata" if k else "_hira") + ".png"

    save_kana(c, v, k, filename)
    print(f"saved to {filename}!")

if __name__ == "__main__":
    main()
