import math

1. 
# print(math.sqrt(114921))

2. 
# when 117 chocolates eqully distributed to x students, we are left by x-9 choco. x=?
# n = 126  # 117 + 9

# solutions = []
# for x in range(1, n + 1):
#     if n % x == 0 and x > 9:          # x must divide 126 and be > 9
#         q = (n // x) - 1              # chocolates per student
#         r = x - 9                     # remainder
#         solutions.append((x, q, r))

# for x, q, r in solutions:
#     print(f"x = {x} -> each student gets {q}, remainder = {r}")

3.
# a person goes at 20 kmph for some time and rest of the time at 60kmph. if avg speed was 30kmph for entire trip, what was the time fraction for 20kph? 
# python code, fast, minimalist

4. 
from sympy import symbols, Eq, solve

f = symbols('f')  # fraction of time at 20 kmph
sol = solve(Eq(20*f + 60*(1-f), 30), f)
print(sol)