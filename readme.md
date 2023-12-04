# Usage

## Save Kana

```
python save_kana.py [-k] <consonant> <vowel>
```

where consonant is `_`, or a valid lowercase Japanese consonant, vowel is one of `a`, `i`, `u`, `e`, `o`, or `_` if no vowel, and `-k` is whether to use katakana.

## Kana Deck

```
python kana_deck.py [-k] <filename>
```

where filename is the write path for the anki deck, and `-k` is whether to use katakana.

## Examples

Saving the `a` hiragana:

```
python save_kana.py _ a
```

Saving the `n` katakana:

```
python save_kana.py -k n _
```

Creating a deck of hiragana:

```
python kana_deck.py hiragana.apkg
```

Creating a deck of katakana:

```
python kana_deck.py katakana.apkg
```

# Credits

To `u/Moer_by` for creating [this chart](https://www.reddit.com/r/japaneseresources/comments/ilkott/hiragana_katakana_stroke_order_chart/).
