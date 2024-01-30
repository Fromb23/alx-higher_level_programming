#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text_1 = text.replace(".", "\n\n")
    text_1 = text_1.replace("?", "\n\n")
    text_1 = text_1.replace(":", "\n\n")

    print(text_1)
