#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first_char = None
    _len = len(sentence)
    first_char = sentence[0]

    return (_len, first_char)
