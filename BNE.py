def toBinary(num: int) -> str:
    n = bin(num)[2:] if num >= 0 else bin(num)[3:]
    return n


def XOR(first, second):
    res, _ = addBinaries(first, second, return_carry=True)
    return res

def intToStraight(num: int):
    binary_repr: str = toBinary(num)
    sign: str = '0' if num >= 0 else '1'
    return Straight(sign, binary_repr)


def intToInversed(num: int):
    binary_repr: str = toBinary(num)
    sign: str = '0' if num >= 0 else '1'
    if num < 0:
        binary_repr = inverseBits(binary_repr)

    return Inverted(sign, binary_repr)


def intToExtended(num: int):
    binary_repr: str = toBinary(num)
    sign: str = '0' if num >= 0 else '1'
    if num < 0:
        binary_repr, _ = addBinaries(inverseBits(binary_repr), '1')

    return Extended(sign, binary_repr)


def inverseBits(binary_repr: str) -> str:
    return str(''.join('1' if digit == '0' else '0' for digit in binary_repr))


def addBinaries(a: str, b: str, return_carry=False, *, outer_carry: str = '0') -> (str, str):
    a, b = a[::-1], b[::-1]
    carry: int = int(outer_carry)
    i: int = 0
    result: str = ''
    while i < len(a):
        if i < len(b):
            res = (int(a[i]) + int(b[i]) + carry)
        else:
            res = (int(a[i]) + carry)
        cur_digit = res % 2
        carry = res // 2
        result = str(cur_digit) + result
        i += 1

    if return_carry:
        return result, str(carry)

    if carry == 1:
        result = str(carry) + result
    return result, '0'


class Straight:
    def __init__(self, sign: str, binary_repr: str) -> None:
        self.binary_repr = binary_repr
        self.sign = sign

    def __neg__(self):
        sign = '1' if self.sign == '0' else '0'
        output = Straight(sign, self.binary_repr)
        return output

    def __str__(self) -> str:
        return self.sign + ',' + self.binary_repr

    def __add__(self, other):
        result, sign = addBinaries(self.binary_repr, other.binary_repr)

        output = Straight(sign, result)

        return output

    def __abs__(self):
        if self.sign == '1':
            return -self
        return self

    def __len__(self):
        return len(self.binary_repr)

    def toStraight(self):
        return self

    def __int__(self) -> int:
        res = int(self.toStraight().binary_repr, 2)
        if self.sign == '1':
            res = -res

        return res

    def equalize(self, length: int):
        return Straight(self.sign, self.binary_repr.rjust(length, '0'))

    def mult(self, n: int):
        res = Straight(self.sign, self.binary_repr.ljust(len(self) + n, '0'))
        return res

    def suffix(self):
        return 'п'


class Inverted(Straight):
    def __neg__(self):
        return Inverted(inverseBits(self.sign), inverseBits(self.binary_repr))

    def __add__(self, other):
        if len(self) > len(other):
            other = other.equalize(len(self))
        elif len(self) < len(other):
            self = self.equalize(len(other))

        result, carry = addBinaries(self.binary_repr, other.binary_repr, True)

        sign, carry = addBinaries(self.sign, other.sign, True, outer_carry=carry)

        output = Inverted(sign, result)
        if carry == '1':
            output = output + Inverted('0', carry)
        return output

    def equalize(self, length: int):
        if self.sign == '1':
            return Inverted(self.sign, self.binary_repr.rjust(length, '1'))
        return Inverted(self.sign, self.binary_repr.rjust(length, '0'))

    def mult(self, n: int):
        if self.sign == '1':
            return Inverted(self.sign, self.binary_repr.ljust(len(self) + n, '1'))
        return Inverted(self.sign, self.binary_repr.ljust(len(self) + n, '0'))

    def toStraight(self):
        if self.sign == '1':
            return Straight(self.sign, inverseBits(self.binary_repr))
        return self

    def suffix(self):
        return 'о'


class Extended(Straight):
    def __neg__(self):
        return Extended(inverseBits(self.sign), addBinaries(inverseBits(self.binary_repr), '1')[0])

    def __add__(self, other):
        if len(self) > len(other):
            other = other.equalize(len(self))
        elif len(self) < len(other):
            self = self.equalize(len(other))

        result, carry = addBinaries(self.binary_repr, other.binary_repr, True)

        sign, carry = addBinaries(self.sign, other.sign, True, outer_carry=carry)
        return Extended(sign, result)

    def __sub__(self, other):
        return self + (-other)

    def toStraight(self):
        if self.sign == '1':
            return Straight(self.sign, addBinaries(inverseBits(self.binary_repr), '1')[0])
        return self

    def equalize(self, length: int):
        if self.sign == '1':
            return Extended(self.sign, self.binary_repr.rjust(length, '1'))
        return Extended(self.sign, self.binary_repr.rjust(length, '0'))

    def mult(self, n: int):
        return Extended(self.sign, self.binary_repr.ljust(len(self) + n, '0'))

    def suffix(self):
        return 'д'