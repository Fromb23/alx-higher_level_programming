#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as e:
        sys.stderr.write('Exception: ' + str(e) + '\n')
        return None
