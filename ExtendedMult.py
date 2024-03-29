from BNE import *
from Output import *


def print_header(X: Straight, Y: Straight):
  X_ext = intToExtended(int(X)).equalize(len(X))
  Y_ext = intToExtended(int(Y)).equalize(len(Y))
  print(
      f'{f"[X]_{X.suffix()} = {str(X)} = {int(X)}/{2 ** len(X)}":>16} {f"[X]_{X_ext.suffix()} = {str(X_ext)} = {int(X)}/{2 ** len(X)}"}'
  )
  print(
      f'{f"[Y]_{Y.suffix()} = {str(Y)} = {int(Y)}/{2 ** len(Y)}":>16} {f"[Y]_{Y_ext.suffix()} = {str(Y_ext)} = {int(Y)}/{2 ** len(Y)}"}'
  )
  print(
      f'{f"-[X]_{X.suffix()} = {str(-X_ext)} = {int(-X_ext)}/{2 ** len(X)}":>16}'
  )

  print(
      f'1. Вычисляем знак: Z_зн = X_зн ⊕ Y_зн = {X.sign} ⊕ {Y.sign} = {XOR(X.sign, Y.sign)}'
  )


def firstMethod(X: Straight, Y: Straight):
  print_header(X, Y)
  target_len = len(X) + len(Y)
  X = intToExtended(int(X)).equalize(len(X))
  Y = intToExtended(int(Y)).equalize(len(Y))
  Y_nums = Y.sign + Y.binary_repr
  sign = XOR(X.sign, Y.sign)

  X_mod = abs(X)

  S = Extended('0', '0' * (target_len))
  for i in range(len(Y) + 1):
    if i == 0:
      printStep(f'Y_{i} = {Y_nums[i]}', S, f'S_{i}')
      if Y_nums[i] == '1':
        printStep(' ',
                  -X,
                  f'-[X]_{X.suffix()} - корерктирующий шаг',
                  is_result=True,
                  is_plus=True)
        S = (-X).mult(len(Y))
      else:
        printStep(' ',
                  X,
                  f'-[X]_{X.suffix()} - корерктирующий шаг',
                  is_result=True,
                  is_plus=True,
                  is_plus_crossed=True)
      printStep(' ', S, f'S_{i}')
    else:
      printStep(f'Y_-{i} = {Y_nums[i]}', S, f'S_{i}')
      if Y_nums[i] == '1':
        printStep(' ',
                  X.equalize(len(X) + i),
                  f'[X]_{X.suffix()} * 2^-{i}',
                  is_result=True,
                  is_plus=True)

        S = S + X.mult(len(Y) - i)
      else:
        printStep(' ',
                  X.equalize(len(X) + i),
                  f'[X]_{X.suffix()} * 2^-{i}',
                  is_result=True,
                  is_plus=True,
                  is_plus_crossed=True)

      printStep(' ', S, f'S_{i+1}')
    print()
  S = S.equalize(len(X) + len(Y))
  printStep(' ', S, f'S_{len(Y) + 1}')
  Z = Extended(sign, S.binary_repr)
  print(f'Результат: [Z]_{Z.suffix()} = {str(Z)}, В десятичной: {frac(Z)}')
  print(
      f'Проверка: X * Y = {frac(X)} * {frac(Y)} = {int(X) * int(Y)}/{2 ** (len(X) + len(Y))}'
  )


def secondMethod(X: Straight, Y: Straight):
  print_header(X, Y)

  X = intToExtended(int(X)).equalize(len(X))
  Y = intToExtended(int(Y)).equalize(len(X))
  target_len = len(X) + len(Y)
  Y_nums = Y.sign + Y.binary_repr + '0'
  sign = XOR(X.sign, Y.sign)
  curent_step = ''

  S = Extended('0', '0' * target_len)
  for i in range(len(Y) + 1):
    curent_step = Y_nums[i:i + 2]
    printStep(f'{curent_step}', S, f'S_{i}')
    match curent_step:
      case '10':
        S = S - X.mult(len(Y) - i)
        printStep(' ', (-X).equalize(len(X) + i),
                  f'-[X]_{X.suffix()} * 2^-{i}',
                  is_result=True,
                  is_plus=True)

      case '01':
        S = S + X.mult(len(Y) - i).equalize(target_len)
        printStep(' ',
                  X.equalize(len(X) + i),
                  f'[X]_{X.suffix()} * 2^-{i}',
                  is_result=True,
                  is_plus=True)
      case _:
        printStep(' ',
                  X.equalize(len(X) + i),
                  f'[X]_{X.suffix()} * 2^-{i}',
                  is_result=True,
                  is_plus=True,
                  is_plus_crossed=True)

    printStep(' ', S, f'S_{i + 1}')
    print()
  if curent_step == '01':
    printStep(f'{"10"}', S, f'S_{len(Y)}')
    S = S + X.mult(len(Y))
    printStep(' ', X, '|X|', is_result=True, is_plus=True)
    printStep(' ', S, f'S_{len(Y)}')
  S = S.equalize(len(X) + len(Y))
  printStep(' ', S, f'S_{len(Y) + 1}')
  Z = Extended(sign, S.binary_repr)
  print(f'Результат: [Z]_{Z.suffix()} = {str(Z)}, В десятичной: {frac(Z)}')
  print(
      f'Проверка: X * Y = {frac(X)} * {frac(Y)} = {int(X) * int(Y)}/{2 ** (len(X) + len(Y))}'
  )
