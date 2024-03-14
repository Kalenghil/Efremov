from typing import Any


def printStep(first: Any, second: Any, third: Any, *, is_plus=False, is_plus_crossed=False, is_result=False):
    if is_result:
        second = underline(f'{str(second):<12}')

    plus = ''

    if is_plus:
        plus = '+'
        if is_plus_crossed:
            plus = "\u04FE"

    print(f'{str(first):^9} {plus:^3} {str(second):<12} {str(third):<6}')

def frac(X):
    return f'{int(X)}/{2**len(X)}'

def math_frac(x):
    num, denom = (int(elem) for elem in frac(x).split(r'/'))
    return num / denom

def underline(text: Any):
    return f"\033[4m{str(text)}\033[0m"

def crossed(text: Any):
    return f"\033[9m{text}\033[0m"
