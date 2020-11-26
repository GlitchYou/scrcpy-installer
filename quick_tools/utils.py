"""
Utils

Run actions easily
"""


def sh(cmd):
    from subprocess import call
    return call(cmd, shell=True)


def cl():
    if __file__[1] == ':':
        sh('cls')
    else:
        sh('clear')


def rsh(cmd):
    from subprocess import getoutput
    return getoutput(cmd)


def reg(string, regex, replace=None):
    """

    Find and replace with regex

    Args:
        string  (str):      Text to search
        regex   (str):      Regex to search
        replace (str):      Replace text groups are replaced with \1 or $1

    Return (str | list):
        Returns the list with the found regex or a replaced string
    """

    from re import findall, sub

    if replace is None:
        return findall(regex, string)

    else:
        replace = sub(r'\$(\d+)', r'\\\1', replace)
        return sub(regex, replace, string)

