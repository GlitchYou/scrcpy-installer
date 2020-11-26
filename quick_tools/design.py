"""
Design

Create custom inputs
"""

from .stylors import *


def lin(text='', sym='-', num=50, center=True):
    from re import findall, sub

    if text == '':
        print(sym * num)

    else:

        colors = findall(r'\x1b\[(?:[\d;]+)?m', text)
        csym = len(sub(r'\x1b\[(?:[\d;]+)?m', '', sym))

        cnum = int(num * csym)

        if len(colors) > 0:
            for n in colors:
                cnum += len(n)

        if center:
            text = text.center(cnum)

        print(sym * num)
        print(text)
        print(sym * num)


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


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except (ValueError, TypeError):
            print(f'{cr}Type an integer{nn}')


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print(f"{cr}Enter a decimal number{nn}")


