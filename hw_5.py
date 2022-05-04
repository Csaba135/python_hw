from math import gcd,lcm
class Fraction:
    def __init__(self, numerator, denominator):
        gcd_num=gcd(numerator, denominator)
        lcm_num=lcm(numerator,denominator)
        self.numerator = numerator//gcd_num
        self.denominator = denominator//gcd_num

    def __add__(self, other):
        new_numerator=self.numerator*other.denominator+other.numerator*self.denominator
        new_denominator=self.denominator*other.denominator
        return Fraction(new_numerator,new_denominator)
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

fraction_1 = Fraction(5,18)
fraction_2 = Fraction(2,3)
fraction_3 = fraction_1+fraction_2
print(fraction_1)
print(fraction_2)
print(fraction_3)

