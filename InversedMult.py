from BNE import *
from Output import *


def print_header(X: Straight, Y: Straight):
  X_inv = intToInversed(int(X)).equalize(len(X))
  Y_inv = intToInversed(int(Y)).equalize(len(Y))
  print(
      f'{f"[X]_{X.suffix()} = {str(X)} = {int(X)}/{2 ** len(X)}":>16} {f"[X]_{X_inv.suffix()} = {str(X_inv)} = {int(X)}/{2 ** len(X)}"}'
  )
  print(
      f'{f"[Y]_{Y.suffix()} = {str(Y)} = {int(Y)}/{2 ** len(Y)}":>16} {f"[Y]_{Y_inv.suffix()} = {str(Y_inv)} = {int(Y)}/{2 ** len(Y)}"}'
  )
  print(
      f'{f"-[X]_{X_inv.suffix()} = {str(-X_inv)} = {int(-X_inv)}/{2 ** len(X)}":>16}'
  )

  print(
      f'1. Вычисляем знак: Z_зн = X_зн ⊕ Y_зн = {X.sign} ⊕ {Y.sign} = {XOR(X.sign, Y.sign)}'
  )


def firstMethod(X: Straight, Y: Straight):
  print_header(X, Y)
  target_len = len(X) + len(Y)
  X = intToInversed(int(X)).equalize(len(X))
  Y = intToInversed(int(Y)).equalize(len(Y))
  Y_nums = Y.sign + Y.binary_repr
  sign = XOR(X.sign, Y.sign)

  X_mod = abs(X)

  S = Inverted('0', '0' * (target_len))
  for i in range(len(Y) + 1):
    if i == 0:
      printStep(f'Y_{i} = {Y_nums[i]}', S, f'S_{i}')
      if Y_nums[i] == '1':
        printStep(' ', (-X).mult(len(Y)),
                  f'-[X]_{X.suffix()} - корерктирующий шаг',
                  is_result=True,
                  is_plus=True)
        S = S + (-X).mult(len(Y))
        printStep(' ', S, f'S_{i}')
        S = S + X.equalize(target_len)
        printStep(' ',
                  X.equalize(target_len),
                  f'+[X]_{X.suffix()} * 2^-{len(X)} - корерктирующий шаг',
                  is_result=True,
                  is_plus=True)

      else:
        printStep(' ',
                  '',
                  f'корректирующие шаги не выполняем',
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
  Z = Inverted(sign, S.binary_repr)
  print(f'Результат: [Z]_{Z.suffix()} = {str(Z)}, В десятичной: {frac(Z)}')
  print(
      f'Проверка: X * Y = {frac(X)} * {frac(Y)} = {int(X) * int(Y)}/{2 ** (len(X) + len(Y))}'
  )


def secondMethod(X: Straight, Y: Straight):
  print_header(X, Y)
  target_len = len(X) + len(Y)
  X = intToInversed(int(X)).equalize(len(X))
  Y = Y.equalize(len(Y))
  Y_nums = Y.binary_repr
  sign = XOR(X.sign, Y.sign)
  if Y.sign == '1':
    print(
        f'Преобразуем разряды множителя [\u1EF8]_{Y.suffix()} = {Y.binary_repr}'
    )
    S = Inverted('0', '0' * (target_len))
    for i in range(len(Y)):
      printStep(f'\u1EF9_-{i + 1} = {Y_nums[i]}', S, f'S_{i}')
      if Y_nums[i] == '1':
        printStep(' ', (-X).mult(len(Y) - i - 1).equalize(target_len),
                  f'-[X]_{X.suffix()} * 2^-{i + 1}',
                  is_result=True,
                  is_plus=True)

        S = S + (-X).mult(len(Y) - i - 1)
      else:
        printStep(' ', (-X).mult(len(Y) - i - 1).equalize(target_len),
                  f'-[X]_{X.suffix()} * 2^-{i + 1}',
                  is_result=True,
                  is_plus=True,
                  is_plus_crossed=True)

      printStep(' ', S, f'S_{i+1}')
      print()
  else:
    print(f'Y > 0 => преобразовывать ничего не надо')
    S = Inverted('0', '0' * (target_len))
    for i in range(len(Y)):
      printStep(f'Y_-{i + 1} = {Y_nums[i]}', S, f'S_{i}')
      if Y_nums[i] == '1':
        printStep(' ', (X).mult(len(Y) - i - 1).equalize(target_len),
                  f'[X]_{X.suffix()} * 2^-{i + 1}',
                  is_result=True,
                  is_plus=True)
        S = S + (X).mult(len(Y) - i - 1)
      else:
        printStep(' ', (X).mult(len(Y) - i - 1).equalize(target_len),
                  f'[X]_{X.suffix()} * 2^-{i + 1}',
                  is_result=True,
                  is_plus=True,
                  is_plus_crossed=True)
      printStep(' ', S, f'S_{i+1}')
      print()
  S = S.equalize(len(X) + len(Y))
  printStep(' ', S, f'S_{len(Y) + 1}')
  Z = Inverted(sign, S.binary_repr)
  print(f'Результат: [Z]_{Z.suffix()} = {str(Z)}, В десятичной: {frac(Z)}')
  print(
      f'Проверка: X * Y = {frac(X)} * {frac(Y)} = {int(X) * int(Y)}/{2 ** (len(X) + len(Y))}'
  )
