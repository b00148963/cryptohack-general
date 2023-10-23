def Egcd(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        x, y, gcd = Egcd(b, a % b)
        return (y, x - (a // b) * y, gcd)
u, v ,g= Egcd(26513, 32321)
print((u, v, g))