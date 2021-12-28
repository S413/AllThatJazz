import numpy as np
from sympy import symbols, Eq, solve
import HSCp as harsea

class O_F(object):
    """
    Blue print class for the  Objective Function you want to employ on HS.

    ...

    """
    
    OF = None
    symbol_dict = {}

    def __init__(self):
        a,b,c,d = symbols('a b c d')
        expr = 5*a**3 + 3*b**2 - 2*c + d 
        self.OF = expr
        self.symbol_dict['a']=a
        self.symbol_dict['b']=b
        self.symbol_dict['c']=c
        self.symbol_dict['d']=d

    def print_OF(self):
        print(self.OF)

    def evaluate(self, coef):
         cost = self.OF.evalf(subs={self.symbol_dict['a']:4, self.symbol_dict['b']:1})
         
         print(cost)
         
         return cost
