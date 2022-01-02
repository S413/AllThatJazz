import numpy as np
from sympy import symbols, Eq, solve
import HSCp as harsea

class ObjectiveFun(object):
    """
    Blue print class for the  Objective Function you want to employ on HS.

    ...

    Define a cost function.
    Create or remove symbols for coefficients as required.
    Use those symbols to create your function.
    __init__ should be all you need to modify.
    Follow the example.

    ...

    You can also choose to bypass sympy.
    Modify the code to your needs.

    """

    def __init__(self):
        a, b = symbols('a b')
        self.symbols = [a,b]
        
        expr = (1-a)**2 + 100*(b-a**2)**2
        self.expr = expr

    def evaluate(self, vals):
        subst = [(self.symbols[i], vals[i]) for i in range(len(self.symbols))]
        res = self.expr.subs(subst)
        
        return res
        
    def print_expr(self):
    	print(self.expr)
    	


