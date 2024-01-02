#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
str2 = " with Python"
print(' '.join(str[str.find("object-oriented programming"):].split(maxsplit=2)[:2]) + str2, end="\n")
