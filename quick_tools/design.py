"""
Design

Create custom inputs
"""
from .stylors import *


def menu(*label, prompt='\n> ', mask='{i}) {p}'):
    from time import sleep as wait
    for i in range(0, len(label)):
        p = label[i]
        i = i + 1
        m = eval(f"f'{mask}'")
        print(m)

    while True:
        try:
            r = int(input(f'{prompt}'))
            if 0 < r <= len(label):
                return r
            else:
                print(f'{cr}Option not found!{nn}')
                wait(1)

        except (ValueError, TypeError):
            print(f'{cr}Type an integer{nn}')
            wait(1)
