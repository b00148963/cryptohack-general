a = 66528
b = 52920

while b:
    a, b = b, a % b

print("gcd(a,b) =", a)