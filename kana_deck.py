from genanki import Note, Deck, Package, BASIC_AND_REVERSED_CARD_MODEL
from argparse import ArgumentParser
from random import randrange
from os import remove

from save_kana import save_kana

replacements = {
    "si": "shi",
    "ti": "chi",
    "tu": "tsu",
    "hu": "fu",
}

def make_kana_deck(katakana: bool, filename: str):
    deck = Deck(randrange(1 << 30, 1 << 31), "Katakana" if katakana else "Hiragana")
    files = []

    def process_cv(consonant: str, vowel: str):
        display_c = consonant.lower() if consonant != "_" else ""
        display_v = vowel.lower() if vowel != "_" else ""

        # save file
        kana_filename = display_c + display_v + ("_kata" if katakana else "_hira") + ".png"

        save_kana(consonant, vowel, katakana, kana_filename)
        files.append(kana_filename)

        # add note
        script = "katakana" if katakana else "hiragana"

        romaji = display_c + display_v
        romaji = replacements.get(romaji, romaji)

        name = f"{script} {romaji}"

        note = Note(model=BASIC_AND_REVERSED_CARD_MODEL, fields=[name, f"<img src={kana_filename}>"])
        deck.add_note(note)

    for consonant in list("_kstnhmyrw"):
        for vowel in list("aiueo"):
            if consonant + vowel in ["yi", "ye", "wu"]:
                continue

            process_cv(consonant, vowel)

    process_cv("N", "_")

    package = Package(deck)
    package.media_files = files

    package.write_to_file(filename)

    for file in files:
        remove(file)

def main():
    parser = ArgumentParser(prog="kana_deck", description="creates an anki deck of either hiragana or katakana")
    parser.add_argument("filename", help="the path to store the deck at")
    parser.add_argument("-k", "--katakana", action="store_true", help="makes the deck only include katakana, or hiragana if absent")

    args = parser.parse_args()
    
    make_kana_deck(args.katakana, args.filename)
    print(f"saved to {args.filename}!")

if __name__ == "__main__":
    main()
