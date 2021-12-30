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
        a, b, c, d, e, f = symbols('a b c d e f')
        self.symbols = [a,b,c,d,e,f]
        
        expr = 5*a**23 - 100*b**12 + 33*c**5 - e**3 + f
        self.expr = expr

    def evaluate(self, vals):
        subst = [(self.symbols[i], vals[i]) for i in range(len(vals))]
        res = self.expr.subs(subst)
        
        return res
        
    def print_expr(self):
    	print(self.expr)
    	


