from genanki import Note, Deck, Package, BASIC_AND_REVERSED_CARD_MODEL
from argparse import ArgumentParser
from random import randrange
from os import remove

from save_kana import save_kana

def make_kana_deck(katakana: bool, filename: str):
    deck = Deck(randrange(1 << 30, 1 << 31), ("Kata" if katakana else "Hira") + "kana")
    files = []

    for consonant in list(" kstnhmyrw"):
        for vowel in list("aiueo"):
            if consonant + vowel in ["yi", "ye", "wu"]:
                continue
            
            filename_c = consonant if consonant != " " else "_"
            kana_filename = filename + filename_c + vowel + ".png"

            save_kana(consonant, vowel, katakana, kana_filename)
            files.append(kana_filename)

            note = Note(model=BASIC_AND_REVERSED_CARD_MODEL, fields=[consonant + vowel, f"<img src={kana_filename}>"])
            deck.add_note(note)

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
