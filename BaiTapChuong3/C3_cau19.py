import math

# Nhập x và n
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
for i in range(n + 1):
    term = x**(2*i + 1) / math.factorial(2*i + 1)
    S += term

print("Giá trị S =", S)