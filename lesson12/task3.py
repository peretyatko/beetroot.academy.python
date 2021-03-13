'''Fraction
Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) with appropriate checking and error handling
```
class Fraction:
pass
x = Fraction(1/2)
y = Fraction(1/4)
x + y == Fraction(3/4)'''



class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
