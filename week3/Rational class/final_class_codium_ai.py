"""
Module providing functionality for rational number operations.
"""

def find_nsd(a, b):
    """
    Compute the greatest common divisor of two integers using Euclid's algorithm.

    Args:
    a (int): First integer.
    b (int): Second integer.

    Returns:
    int: Greatest common divisor of a and b.
    """
    if b == 0:
        return a
    return find_nsd(b, a % b)

class Rational:
    """
    Class to represent a rational number as a fraction.
    """
    def __init__(self, numerator, denominator) -> None:
        """
        Initialize a Rational object ensuring the denominator is not zero and is positive.

        Args:
        numerator (int): The numerator part of the rational number.
        denominator (int): The denominator part of the rational number, must not be zero.

        Raises:
        ValueError: If the denominator is zero.
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        """
        String representation of the Rational object.

        Returns:
        str: String representation of the rational number.
        """
        return f'{self.numerator}/{self.denominator}'

    def reduce(self):
        """
        Reduce the rational number by dividing both numerator and denominator by their GCD.

        Returns:
        Rational: The reduced rational number.
        """
        nsd = find_nsd(self.numerator, self.denominator)
        self.numerator //= nsd
        self.denominator //= nsd
        return self

    def __add__(self, other):
        """
        Add two rational numbers.

        Args:
        other (Rational): Another rational number to add.

        Returns:
        Rational: The sum of self and other, reduced to lowest terms.
        """
        nsk = self.denominator * other.denominator // find_nsd(self.denominator, other.denominator)
        dil = nsk // self.denominator
        dal = nsk // other.denominator
        new_numerator = dil * self.numerator + dal * other.numerator
        return Rational(new_numerator, nsk).reduce()

    def __sub__(self, other):
        """
        Subtract another rational number from this one.

        Args:
        other (Rational): Another rational number to subtract.

        Returns:
        Rational: The difference of self and other, reduced to lowest terms.
        """
        nsk = self.denominator * other.denominator // find_nsd(self.denominator, other.denominator)
        dil = nsk // self.denominator
        dal = nsk // other.denominator
        new_numerator = dil * self.numerator - dal * other.numerator
        return Rational(new_numerator, nsk).reduce()

    def __mul__(self, other):
        """
        Multiply two rational numbers.

        Args:
        other (Rational): Another rational number to multiply by.

        Returns:
        Rational: The product of self and other, reduced to lowest terms.
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator).reduce()

    def __truediv__(self, other):
        """
        Divide this rational number by another.

        Args:
        other (Rational): Another rational number to divide by.

        Returns:
        Rational: The quotient of self and other, reduced to lowest terms.
        """
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator).reduce()

    def __eq__(self, other) -> bool:
        """
        Check equality of two rational numbers.

        Args:
        other (Any): Another object to compare.

        Returns:
        bool: True if both rational numbers are equal, False otherwise.
        """
        reduced_self = self.reduce()
        reduced_other = other.reduce()
        return reduced_self.numerator == reduced_other.numerator and \
            reduced_self.denominator == reduced_other.denominator

    def __lt__(self, other) -> bool:
        """
        Check if this rational number is less than another.

        Args:
        other (Rational): Another rational number to compare.

        Returns:
        bool: True if self is less than other, False otherwise.
        """
        reduced_self = self.reduce()
        reduced_other = other.reduce()
        nsk = reduced_self.denominator * reduced_other.denominator \
            // find_nsd(reduced_self.denominator, reduced_other.denominator)
        self_numerator_in_common = nsk // reduced_self.denominator * reduced_self.numerator
        other_numerator_in_common = nsk // reduced_other.denominator * reduced_other.numerator
        return self_numerator_in_common < other_numerator_in_common

    def __le__(self, other) -> bool:
        """
        Check if this rational number is less than or equal to another.

        Args:
        other (Rational): Another rational number to compare.

        Returns:
        bool: True if self is less than or equal to other, False otherwise.
        """
        return self < other or self == other

    def __gt__(self, other) -> bool:
        """
        Check if this rational number is greater than another.

        Args:
        other (Rational): Another rational number to compare.

        Returns:
        bool: True if self is greater than other, False otherwise.
        """
        return not self <= other

    def __ge__(self, other) -> bool:
        """
        Check if this rational number is greater than or equal to another.

        Args:
        other (Rational): Another rational number to compare.

        Returns:
        bool: True if self is greater than or equal to other, False otherwise.
        """
        return not self < other

    @property
    def mixed_form(self):
        """
        Get the mixed number form of the rational number.

        Returns:
        str: The mixed number form of the rational number.
        """
        reduced = self.reduce()
        whole = reduced.numerator // reduced.denominator
        numerator = abs(reduced.numerator) % reduced.denominator

        if reduced.numerator < 0 and numerator != 0:
            whole += 1

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
            if whole < 0 and num > 0:
                num = -num
            self.numerator = whole * denom + num
            self.denominator = denom
        elif isinstance(value, int):
            self.numerator = value
            self.denominator = 1
