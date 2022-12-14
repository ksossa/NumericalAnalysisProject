import numpy as np
from sympy import *
import sympy as sm
from sympy.parsing.sympy_parser import parse_expr

def polynomNewton(table,n):
    polynom = str(table[0][1])
    coef = []
    coef.append(str(table[0][1]))
    for j in range(2,n+1):
        for i in range(j-1,n):
            table[i][j] = (table[i][j-1] - table[i-1][j-1])/(table[i][0] - table[i-j+1][0])
            
            if(i==j-1):
                coef.append(table[i][j])
                polynom += " + " + str(table[i][j])
                for i in range(0,i):
                    polynom += "(x - " + str(table[i][0]) + ")"
    return table,polynom,coef

def newton_interpolation(x, y):
    n = len(x)
    table = np.zeros((n+1,n+1))

    for i in range(n):
        table[i][0] = x[i]
        table[i][1] = y[i]
        
    res,polynom,coef = polynomNewton(table,n)
    res = res.tolist()
    for i in range(len(res)):
        res[i].pop(0)
    res.pop()
    # Divided Difference Table, polynom, coefficients
    print(polynom)
    transformations = (sm.parsing.sympy_parser.standard_transformations +
    (sm.parsing.sympy_parser.implicit_multiplication_application,))
    f = sm.parse_expr(polynom,transformations=transformations)
    polynom = str(sm.sympify(f)).replace("**","^")
    return np.array(res).tolist(),polynom,coef

# print(newton_interpolation([1,3,5],[2,4,6]))