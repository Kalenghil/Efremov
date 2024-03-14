from BNE import *
from Output import *


def print_header(X: Straight, Y: Straight):
    X_ext = intToExtended(int(X))
    Y_ext = intToExtended(int(Y))
    print(f'{f'[X]_{X.suffix()} = {str(X)} = {int(X)}/{2 ** len(X)}':>16}')
    print(f'{f'[Y]_{Y.suffix()} = {str(Y)} = {int(Y)}/{2 ** len(Y)}':>16} {f'-[Y]_{Y_ext.suffix()} = {str(-Y_ext)} = {int(-Y)}/{2 ** len(Y)}'}')



def firstMethod(X: Straight, Y:Straight, digits_after_comma=4):
    print_header(X, Y)
    Y_ext = intToExtended(-int(abs(Y)))
    i = 0
    target_len = digits_after_comma + len(X)
    trash = intToExtended(int(X)).mult(digits_after_comma)
    Z = Straight('', '')
    while i <= digits_after_comma:
        if i == 0:
            printStep('', trash, '|X|')
            printStep('', Y_ext, '-|Y|', is_plus=True, is_result=True)
            trash = trash + Y_ext.mult(digits_after_comma - i)
            if trash.sign == '1':
                Z.sign = '0'
                printStep(f'a_{i} < 0', trash, f'a_{i} < 0, => Z_{i} = 0')
                printStep('', (-Y_ext).mult(digits_after_comma - i).equalize(target_len), '+|Y| - восстановление остатка', is_plus=True, is_result=True)
                trash = trash + (-Y_ext).mult(digits_after_comma - i)
                printStep('', trash, '- восстановленный остатток')
            else:
                Z.sign = '1'
                printStep('', trash, f'a_{i} > 0, => Z_{i} = 1')
        else:
            printStep('', Y_ext.mult(digits_after_comma - i).equalize(target_len), f'-|Y| * 2^{i}', is_plus=True, is_result=True)
            trash = trash + Y_ext.mult(digits_after_comma - i)
            if trash.sign == '1':
                Z.binary_repr += '0'
                printStep(f'a_{i} < 0', trash, f'a_{i} < 0, => Z_{i} = 0')
                printStep('', Y_ext.mult(digits_after_comma - i).equalize(target_len), f'+|Y| * 2^{i}', is_plus=True, is_result=True)
                trash = trash - Y_ext.mult(digits_after_comma - i)
                printStep('', trash, f'- восстановленный остаток')
            else:
                Z.binary_repr += '1'
                printStep('', trash, f'a_{i} > 0, => Z_{i} = 1')
        i += 1
    print(f'[Z]_{Z.suffix()} = {str(Z)} = {frac(Z)} = {math_frac(Z):.4f}')
    print(f'Правильный результат: {int(X)}/{int(Y)} = {int(X)/int(Y):.4f}')
    print(f'Погрешность составила: {abs(math_frac(Z) - int(X)/int(Y)):.4f}')


def secondMethod(X: Straight, Y:Straight, digits_after_comma=4):
    print_header(X, Y)
    Y_ext = intToExtended(-int(abs(Y)))
    i = 0
    target_len = digits_after_comma + len(X)
    trash = intToExtended(int(X)).mult(digits_after_comma)
    Z = Straight('', '')

    printStep('', trash, '|X|')
    printStep('', Y_ext, '-|Y|', is_plus=True, is_result=True)

    trash = trash + Y_ext.mult(digits_after_comma - i)

    for i in range(1, digits_after_comma + 2):
        if trash.sign == '1':
            Z.binary_repr += '0'
            printStep('', trash, f'a_{i} < 0, => Z_{i} = 0')
            printStep('', (-Y_ext).mult(digits_after_comma - i).equalize(target_len), f'+|Y| * 2^-{i}',
                      is_plus=True, is_result=True)
            trash = trash + (-Y_ext).mult(digits_after_comma - i)
        else:
            Z.binary_repr += '1'
            printStep('', trash, f'a_{i} > 0, => Z_{i} = 1')
            printStep('', (Y_ext).mult(digits_after_comma - i).equalize(target_len), f'+|Y| * 2^-{i}',
                      is_plus=True, is_result=True)
            trash = trash + (Y_ext).mult(digits_after_comma - i)

    Z.sign, Z.binary_repr = Z.binary_repr[0], Z.binary_repr[1:]
    print(f'[Z]_{Z.suffix()} = {str(Z)} = {frac(Z)} = {math_frac(Z):.4f}')
    print(f'Правильный результат: {int(X)}/{int(Y)} = {int(X)/int(Y):.4f}')
    print(f'Погрешность составила: {abs(math_frac(Z) - int(X)/int(Y)):.4f}')


