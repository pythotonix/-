''' retional '''
from typing import Any

def find_nsd(a, b):
    ''' нсд '''
    if b == 0:
        return a
    return find_nsd(b, a % b)

class Rational:
    ''' class rational '''
    def __init__(self, numerator, denominator) -> None:
        ''' init method '''
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        ''' str method '''
        return f'{self.numerator}/{self.denominator}'

    def reduce(self):
        ''' reduce '''
        nsd = find_nsd(self.numerator, self.denominator)
        self.numerator //= nsd
        self.denominator //= nsd
        return self

    def __add__(self, other):
        ''' + '''
        nsk = self.denominator * other.denominator // find_nsd(self.denominator, other.denominator)
        dil = nsk // self.denominator
        dal = nsk // other.denominator
        new_numerator = dil * self.numerator + dal * other.numerator
        return Rational(new_numerator, nsk).reduce()

    def __sub__(self, other):
        ''' - '''
        nsk = self.denominator * other.denominator // find_nsd(self.denominator, other.denominator)
        dil = nsk // self.denominator
        dal = nsk // other.denominator
        new_numerator = dil * self.numerator - dal * other.numerator
        return Rational(new_numerator, nsk).reduce()

    def __mul__(self, other):
        ''' * '''
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator).reduce()

    def __truediv__(self, other):
        ''' / '''
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator).reduce()

    def __eq__(self, other) -> bool:
        ''' == '''
        reduced_self = self.reduce()
        reduced_other = other.reduce()
        return reduced_self.numerator == reduced_other.numerator and \
            reduced_self.denominator == reduced_other.denominator

    def __lt__(self, other) -> bool:
        ''' < '''
        reduced_self = self.reduce()
        reduced_other = other.reduce()
        nsk = reduced_self.denominator * reduced_other.denominator \
            // find_nsd(reduced_self.denominator, reduced_other.denominator)
        self_numerator_in_common = nsk // reduced_self.denominator * reduced_self.numerator
        other_numerator_in_common = nsk // reduced_other.denominator * reduced_other.numerator
        return self_numerator_in_common < other_numerator_in_common

    def __le__(self, other) -> bool:
        ''' <= '''
        return self < other or self == other

    def __gt__(self, other) -> bool:
        ''' > '''
        return not self <= other

    def __ge__(self, other) -> bool:
        ''' >= '''
        return not self < other

    @property
    def mixed_form(self):
        ''' mised form property '''
        reduced = self.reduce()
        whole = reduced.numerator // reduced.denominator
        numerator = abs(reduced.numerator) % reduced.denominator
        if numerator == 0:
            return str(whole)
        if whole == 0:
            return f"{numerator}/{reduced.denominator}"
        return f"{whole} {numerator}/{reduced.denominator}"

    @mixed_form.setter
    def mixed_form(self, value):
        ''' setter '''
        if isinstance(value, str):
            parts = value.strip().split(' ')
            if "/" in parts[-1]:
                num, denom = parts[-1].strip().split('/')
                whole = int(parts[0]) if len(parts) > 1 else 0
            else:
                num, denom = parts[-1], 1
                whole = int(parts[0])
            num, denom = int(num), int(denom)
            self.numerator = whole * denom + num
            self.denominator = denom
        elif isinstance(value, int):
            self.numerator = value
            self.denominator = 1
