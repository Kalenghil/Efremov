from BNE import *
from Output import printStep, frac

def print_header(X: Straight, Y: Straight):
    print(f'[X]_{X.suffix()} = {str(X)} = {int(X)}/{2 ** len(X)}')
    print(f'[Y]_{X.suffix()} = {str(Y)} = {int(Y)}/{2 ** len(Y)}')
    X_ext = intToExtended(int(X))
    X_ext = -X_ext

    print(f'[-|X|]_{X_ext.suffix()} = {str(X_ext)} = {int(X_ext)}/{2 ** len(X_ext)}')

    print(f'1. Вычисляем знак: Z_зн = X_зн ⊕ Y_зн = {X.sign} ⊕ {Y.sign} = {XOR(X.sign, Y.sign)}')


def ButMethod(X: Straight, Y: Straight):
    print_header(X, Y)

    Y_nums = Y.binary_repr + '0'
    sign = XOR(X.sign, Y.sign)

    X_mod = abs(X)
    X_ext = intToExtended(int(X))

    S = Extended('0', '0' * (len(X) - 1))
    for i in range(len(Y) - 1, -1, -1):
        S = S.equalize(len(S) + 1)
        curent_step = Y_nums[i:i+2]
        printStep(f'{curent_step}', S, f'S_{len(Y) - i - 1} * 2^-1')
        match curent_step:
            case '10':
                S = S - X_ext.mult(len(Y) - i - 1)
                printStep(' ', -X_ext, '-|X|', is_result=True, is_plus=True)

            case '01':
                S = S + X_ext.mult(len(Y) - i - 1)
                printStep(' ', X_ext, '|X|', is_result=True, is_plus=True)
            case _:
                printStep(' ', '', 'не меняем', is_result=True, is_plus=True, is_plus_crossed=True)

        printStep(' ', S, f'S_{len(Y) - i}')
        print()
    S = S.equalize(len(X) + len(Y))
    printStep(' ', S, f'S_{len(Y)} * 2^-1')
    Z = Straight(sign, S.binary_repr)
    print(f'Результат: [Z]_{Z.suffix()} = {str(Z)}, В десятичной: {frac(Z)}')
    print(f'Проверка: X * Y = {frac(X)} * {frac(Y)} = {int(X) * int(Y)}/{2 ** (len(X) + len(Y))}')


def ButMethod(X: Straight, Y: Straight):
    print_header(X, Y)

    Y_nums = Y.binary_repr + '0'
    sign = XOR(X.sign, Y.sign)

    X_mod = abs(X)
    X_ext = intToExtended(int(X))

    S = Extended('0', '0' * (len(X) - 1))
    for i in range(len(Y) - 1, -1, -1):
        S = S.equalize(len(S) + 1)
        curent_step = Y_nums[i:i+2]
        printStep(f'{curent_step}', S, f'S_{len(Y) - i - 1} * 2^-1')
        match curent_step:
            case '10':
                S = S - X_ext.mult(len(Y) - i - 1)
                printStep(' ', -X_ext, '-|X|', is_result=True, is_plus=True)

            case '01':
                S = S + X_ext.mult(len(Y) - i - 1)
                printStep(' ', X_ext, '|X|', is_result=True, is_plus=True)
            case _:
                printStep(' ', '', 'не меняем', is_result=True, is_plus=True, is_plus_crossed=True)

        printStep(' ', S, f'S_{len(Y) - i}')
        print()
    S = S.equalize(len(X) + len(Y))
    printStep(' ', S, f'S_{len(Y)} * 2^-1')
    Z = Straight(sign, S.binary_repr)
    print(f'Результат: [Z]_{Z.suffix()} = {str(Z)}, В десятичной: {frac(Z)}')
    print(f'Проверка: X * Y = {frac(X)} * {frac(Y)} = {int(X) * int(Y)}/{2 ** (len(X) + len(Y))}')


def PairMethod(X: Straight, Y: Straight):
    print_header(X, Y)

    Y_nums = Y.binary_repr + '0'
    sign = XOR(X.sign, Y.sign)

    X_mod = abs(X)
    X_ext = intToExtended(int(X))
    correction = '0'

    S = Extended('0', '0' * (len(X) - 2))
    for i in range(len(Y) - 1, -1, -2):
        S = S.equalize(len(S) + 2)
        curent_step, correction = addBinaries(Y_nums[i-1:i+1], str(correction), True)
        printStep(f'{curent_step}   +{correction}', S, f'S_{len(Y) - i - 1} * 2^-1')
        match curent_step:
            case '01':
                S = S + X_ext.mult(len(Y) - i - 1)
                printStep(' ', X_ext, '+|X|', is_result=True, is_plus=True)

            case '10':
                S = S + X_ext.mult(len(Y) - i)
                printStep(' ', X_ext, '+2|X|', is_result=True, is_plus=True)

            case '11':
                S = S - X_ext.mult(len(Y) - i - 1)
                printStep(' ', -X_ext, '-|X|', is_result=True, is_plus=True)
                correction, _ = addBinaries(correction, '1', True)

            case _:
                printStep(' ', '', 'не меняем', is_result=True, is_plus=True, is_plus_crossed=True)

        printStep(' ', S, f'S_{len(Y) - i}')
        print()
    if correction == '1':
        S = S.equalize(len(S) + 2)
        curent_step, correction = addBinaries(Y_nums[i - 1:i + 1], str(correction), True)
        printStep(f'{curent_step}   +{correction}', S, f'S_{len(Y) - i - 1} * 2^-1')
        S = S + X_ext.mult(len(Y))
        printStep(' ', X_ext, '+|X|', is_result=True, is_plus=True)

    S = S.equalize(len(X) + len(Y))
    printStep(' ', S, f'S_{len(Y)} * 2^-1')
    Z = Straight(sign, S.binary_repr)
    print(f'Результат: [Z]_{Z.suffix()} = {str(Z)}, В десятичной: {frac(Z)}')
    print(f'Проверка: X * Y = {frac(X)} * {frac(Y)} = {int(X) * int(Y)}/{2 ** (len(X) + len(Y))}')
