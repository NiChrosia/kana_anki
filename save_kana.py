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
CONSONANTS = list(" kstnhmyrwn")

all_kana: Image.Image | None = None

def find_kana(c: str, v: str, katakana: bool) -> tuple[int, int]:
    c_index = CONSONANTS.index(c)
    v_index = VOWELS.index(v)

    x = START_X + HORIZ_OFFSET * v_index
    y = START_Y + VERT_OFFSET * c_index

    if katakana:
        x += KATA_OFFSET

    return (x, y)

def save_kana(c: str, v: str, katakana: bool, filename: str):
    """value in the format cvk, where v is a japanese vowel, c is a 
    japanese consonant, and k is h or k, meaning hira- or kata-kana"""

    global all_kana

    if not all_kana:
        all_kana = Image.open("kana.png")

    x, y = find_kana(c, v, katakana)

    kana = all_kana.copy().crop((x, y, x + TILE_WIDTH - 1, y + TILE_HEIGHT - 1))
    kana.save(filename)

def main():
    parser = ArgumentParser(prog="save_kana", description="saves the stroke order for a specified kana")
    parser.add_argument("consonant", help="the lowercase character of the consonant, or _ for no consonant")
    parser.add_argument("vowel", help="the vowel of the kana (aiueo)")
    parser.add_argument("-k", "--katakana", action="store_true", help="whether to use katakana, or hiragana if absent")

    args = parser.parse_args()

    c = args.consonant
    v = args.vowel
    k = args.katakana

    find_kana_c = c if c != "_" else " "

    filename_c = c if c != "_" else ""
    filename_k = "_kata" if k else "_hira"

    filename = filename_c + v + filename_k + ".png"

    save_kana(find_kana_c, v, k, filename)
    print(f"saved to {filename}!")

if __name__ == "__main__":
    main()
