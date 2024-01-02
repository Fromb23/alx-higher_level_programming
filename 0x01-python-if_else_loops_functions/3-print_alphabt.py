#!/usr/bin/python3

for i in range(97, 123):
    if chr(i) not in {'q', 'e'}:    
        print("{:c}".format(i), end="")
