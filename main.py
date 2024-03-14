from BNE import *
import sys

import StraightMult
import FastMult
import ExtendedMult
import InversedMult
import Division

DEBUG_MODE = False


def print_divider():
  print()
  print("= = = = = = = = = = = = = = = = = = = = = = = = = =")
  print()


from Output import underline, printStep
if __name__ == "__main__":
  if DEBUG_MODE:
    num1 = Straight('0', '1111')
    num2 = Straight('0', '1111')

    # firstMethod(num1, num2)
    # secondMethod(num1, num2)
    # thirdMethod(num1, num2)
    # fourthMethod(num1, num2)

    num1 = Straight('0', '1111')
    num2 = Straight('0', '1111')
    # num2 = intToExtended(-int(num1)).mult(4)
    # num1 = Extended('0', '000000')
    # print(num1, num2, num1 + num2)

    FastMult.PairMethod(num1, num2)
    sys.exit('0')
  while True:
    print_divider()
    print(
        "Вводить числа необходимо в прямом коде, в формате <знаковый бит>,<остальная часть>"
    )
    print('Примеры: 1,1001')
    X = input("Введите число X: ")
    Y = input("Введите число Y: ")
    try:
      X = Straight(X[0], X[2:])
      Y = Straight(Y[0], Y[2:])
    except Exception:
      print("Вы неправильно ввели числа")
      continue

    print_divider()
    variant = ''
    print("Выберите тип задачи: ")
    print("1 Умножение в прямом коде")
    print("2 Ускоренные алгоритмы умножения")
    print("3 Умножение в дополнительном коде")
    print("4 Умножение в обратном коде")
    print("5 Деление в прямом коде")
    variant = input("Ваш выбор: ")
    match variant:
      case '1':
        print_divider()
        print('Вы выбрали умноение в прямом коде')
        print('Выберете метод умножения: ')
        print("1 Первый способ")
        print("2 Втрорй способ")
        print("3 Третий способ")
        print("4 Четвёртый способ")
        method = input("Ваш выбор: ")
        match method:
          case '1':
            StraightMult.firstMethod(X, Y)
          case '2':
            StraightMult.secondMethod(X, Y)
          case '3':
            StraightMult.thirdMethod(X, Y)
          case '4':
            StraightMult.fourthMethod(X, Y)
          case _:
            print("Неверный выбор")
      case '2':
        print_divider()
        print('Вы выбрали ускоренные алгоритмы умножения')
        print(
            '''Алгоритмы не работают с отрицательными числами, не знаю баг это или фича, \n
               но на всякий случай сверяйте ответы c проверкой''')
        print('Выберете метод умножения: ')
        print("1 Алгоритм Бута")
        print("2 Алгоритм выборки по два знака")
        method = input("Ваш выбор: ")
        match method:
          case '1':
            FastMult.ButMethod(X, Y)
          case '2':
            FastMult.PairMethod(X, Y)
          case _:
            print("Неверный выбор")
      case '3':
        print_divider()
        print('Вы выбрали умножение в дополнительном коде')
        print('Выберете метод умножения: ')
        print("1 Первый способ")
        print("2 Втрорй способ")
        method = input("Ваш выбор: ")
        match method:
          case '1':
            ExtendedMult.firstMethod(X, Y)
          case '2':
            ExtendedMult.secondMethod(X, Y)
          case _:
            print("Неверный выбор")
      case '4':
        print_divider()
        print('Вы выбрали умножение в обратном коде')
        print('Выберете метод умножения: ')
        print("1 Первый способ")
        print("2 Втрорй способ")
        method = input("Ваш выбор: ")
        match method:
          case '1':
            InversedMult.firstMethod(X, Y)
          case '2':
            InversedMult.secondMethod(X, Y)
          case _:
            print("Неверный выбор")
      case '5':
        print_divider()
        print('Вы выбрали деление в прямом коде')
        print('Выберете метод деления: ')
        print("1 Первый способ")
        print("2 Втрорй способ")
        method = input("Ваш выбор: ")
        match method:
          case '1':
            Division.firstMethod(X, Y)
          case '2':
            Division.secondMethod(X, Y)
          case _:
            print("Неверный выбор")
      case _:
        print("Неверный выбор")
