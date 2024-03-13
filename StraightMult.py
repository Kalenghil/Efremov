from BNE import *
from Output import printStep, frac


def print_header(X: Straight, Y: Straight):
    print(f'[X]_{X.suffix()} = {str(X)} = {int(X)}/{2 ** len(X)}')
    print(f'[Y]_{X.suffix()} = {str(Y)} = {int(Y)}/{2 ** len(Y)}')

    print(f'1. Вычисляем знак: Z_зн = X_зн ⊕ Y_зн = {X.sign} ⊕ {Y.sign} = {XOR(X.sign, Y.sign)}')


def firstMethod(X: Straight, Y: Straight):
    print_header(X, Y)

    Y_nums = Y.binary_repr
    sign = XOR(X.sign, Y.sign)

    X_mod = abs(X)

    S = Straight('0', '0'*(len(X)-1))
    for i in range(len(Y) - 1, -1, -1):
        S = S.equalize(len(S) + 1)
        printStep(f'Y_-{i} = {Y_nums[i]}', S, f'S_{len(Y) - i - 1} * 2^-1')
        if Y_nums[i] == '1':
            printStep(' ', X, '|X|', is_result=True, is_plus=True)

            S = S + X_mod.mult(len(Y) - i - 1)
        else:
            printStep(' ', X_mod, '|X|', is_result=True, is_plus=True, is_plus_crossed=True)

        printStep(' ', S, f'S_{len(Y) - i}')
        print()
    S = S.equalize(len(X) + len(Y))
    printStep(' ', S, f'S_{len(Y)} * 2^-1')
    Z = Straight(sign, S.binary_repr)
    print(f'Результат: [Z]_{Z.suffix()} = {str(Z)}, В десятичной: {frac(Z)}')
    print(f'Проверка: X * Y = {frac(X)} * {frac(Y)} = {int(X) * int(Y)}/{2**(len(X) + len(Y))}')


def secondMethod(X: Straight, Y: Straight):
    print_header(X, Y)

    Y_nums = Y.binary_repr
    sign = XOR(X.sign, Y.sign)

    X_mod = abs(X)

    S = Straight('0', '0'*(len(X) + len(Y)))
    for i in range(len(Y) - 1, -1, -1):
        printStep(f'Y_-{i} = {Y_nums[i]}', S, f'S_{len(Y) - i - 1}')
        if Y_nums[i] == '1':
            printStep(' ', f'{' '*(i+3) + X_mod.binary_repr}', f'|X| * 2^{i + 1}', is_result=True, is_plus=True)

            S = S + X_mod
        else:
            printStep(' ', f'{' '*(i+3) + X_mod.binary_repr}', f'|X| * 2^{i + 1}', is_result=True, is_plus=True, is_plus_crossed=True)
        X_mod = X_mod.mult(1)

        printStep(' ', S, f'S_{len(Y) - i}')
        print()
    S = S.equalize(len(X) + len(Y))
    printStep(' ', S, f'S_{len(Y)} * 2^-1')
    Z = Straight(sign, S.binary_repr)
    print(f'Результат: [Z]_{Z.suffix()} = {str(Z)}, В десятичной: {frac(Z)}')
    print(f'Проверка: X * Y = {frac(X)} * {frac(Y)} = {int(X) * int(Y)}/{2**(len(X) + len(Y))}')

