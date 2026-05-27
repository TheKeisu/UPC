from sympy import solve, symbols, expand
x = symbols('x')
print(solve(expand((x + 2)**2)))
