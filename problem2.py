problem = "problem2"
student_name = "Beemnet_Amdissa_Teshome"
student_number = "T0338757"

from math import gcd
# define your Fraction class in this file

class Fraction:
    """Fraction class with dunder methods and other methods"""

    # object initializer 
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        self.numerator = numerator
        self.denominator = denominator

    # display fraction as a string
    def __str__(self):
        num_str = str(self.numerator)
        den_str = str(self.denominator)

        return f"{num_str}/{den_str}"
    
    # add fractions and return object
    def __add__(self, other):
        sum_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        sum_denominator = self.denominator * other.denominator
        
        return Fraction(sum_numerator, sum_denominator)
    
    # subtract fractions and return object
    def __sub__(self, other):
        sub_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        sub_denominator = self.denominator * other.denominator

        return Fraction(sub_numerator, sub_denominator)
    
    # return fraction as a float
    def __float__(self):
        return self.numerator/self.denominator
    
    # multiply fractions and return object
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    # divide fractions and return object
    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Can't divide by zero.")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
    
    # check fractions for equality, return boolean (True or False)
    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    # reverse fraction 
    def inverse(self):
        return f"{self.denominator}/{self.numerator}"
    
    # reduce fraction to simplest form using greatest common divisor and return object
    def reduce(self):
        common_divisor = gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // common_divisor, self.denominator // common_divisor)

    
    

