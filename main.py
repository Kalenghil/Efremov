from BNE import *
from StraightMult import *
from FastMult import *
import ExtendedMult
import InversedMult
import Division
from Output import underline, printStep
if __name__ == "__main__":
    num1 = Straight('1', '1001')
    num2 = Straight('0', '1101')

    # firstMethod(num1, num2)
    # secondMethod(num1, num2)
    # thirdMethod(num1, num2)
    # fourthMethod(num1, num2)

    num1 = Straight('0', '1001')
    num2 = Straight('0', '1011')
    # num2 = intToExtended(-int(num1)).mult(4)
    # num1 = Extended('0', '000000')
    # print(num1, num2, num1 + num2)

    Division.secondMethod(num1, num2)
