######################################################################################################################
# Name: Daniel Taylor
# Date: 1/14/22
# Description: Fraction Classes
######################################################################################################################

# the fraction class
class Fraction():
    def __init__(self, num = 0, den = 1):
        self._num = num
        self._den = den
        self.reduce()

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    
    @property
    def den(self):
        return self._den
    
    @den.setter
    def den(self, value):
        if value != 0:
            self._den = value
        else:
            self._den = 1
            

    def to_decimal(self):
        return self.num / self.den

    def reduce(self):
        gcd = 1
        minimum = min(self.num, self.den)
        for i in range(2, int(minimum) + 1):
            if self.num % i == 0 and self.den % i == 0:
                gcd = i
        
        self.num = int(self.num / gcd)
        self.den = int(self.den / gcd)
        if self.num == 0:
            self.den == 1

    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        result = Fraction(num, den)
        result.reduce()
        return result

    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        result = Fraction(num, den)
        result.reduce()
        return result

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        result = Fraction(num, den)
        result.reduce()
        return result

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        result = Fraction(num, den)
        result.reduce()
        return result

    def __str__(self):  
        return (f"{self.num}/{self.den}  ({self.to_decimal()})")
    

# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print("f1:", f1)
print("f2:", f2)
print("f3:", f3)
print("f4:", f4)

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print()
print("f1:", f1)
print("f2:", f2)
print("f3:", f3)
print("f4:", f4)