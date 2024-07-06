#!/usr/bin/python3
"""Doc"""


def text_indentation(text):
    """Doc"""
    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")
    hola = True
    for letter in text:
        if letter in (".", "?", ":"):
            print(letter, end="\n\n")
            hola = False
            continue
        if hola is True and letter == " ":
            print(letter, end="")
        hola = True
