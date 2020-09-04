#积分
# -*- coding: UTF-8 -*-
import types
def integration(func, a, b):
    if not isinstance(func,  types.FunctionType):
        raise Exception("func must be a function")
    if not isinstance(a, int) and not isinstance(a, float) and not isinstance(a, long):
        raise Exception("a must be a number")
    if not isinstance(b, int) and not isinstance(b, float) and not isinstance(b, long):
        raise Exception("b must be a number")
    if a > b:
        raise Exception("a must be smaller than b")
    n = 1000.
    step = (float(b) - float(a) + 1.) / n
    i = a
    total = 0.
    while i <= b and (i + step) <= b:
        total += func(i) * step
        i += step
    return total
   
def squar(x):
    return float(x) * float(x)     
    
if __name__ == "__main__":
    result = integration(squar, 2, 4)
    print(result)
