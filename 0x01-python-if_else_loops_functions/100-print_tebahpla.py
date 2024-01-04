#!/usr/bin/python3
result = ""
for i in range(122, 96, -2):
    result += chr(i)
    result += chr(i - 33)

print(result)
