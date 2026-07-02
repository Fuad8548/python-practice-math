import math

# print(math.sqrt(114921))

# when 117 chocolates eqully distributed to x students, we are left by x-9 choco. x=?
n = 126  # 117 + 9

solutions = []
for x in range(1, n + 1):
    if n % x == 0 and x > 9:          # x must divide 126 and be > 9
        q = (n // x) - 1              # chocolates per student
        r = x - 9                     # remainder
        solutions.append((x, q, r))

for x, q, r in solutions:
    print(f"x = {x} -> each student gets {q}, remainder = {r}")