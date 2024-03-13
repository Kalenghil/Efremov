from BNE import *
from StraightMult import *
from Output import underline, printStep
if __name__ == "__main__":
    num1 = Straight('1', '1001')
    num2 = Straight('0', '1101')
    print(int(num1), int(num2))

    print(underline(num1 + num2))

    # firstMethod(num1, num2)
    secondMethod(num1, num2)
