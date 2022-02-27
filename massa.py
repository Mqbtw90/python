s=int(input("введите число 1"))
n=int(input("введитe число 2"))
p=int(input("введите число 3"))
r=p/100
m = (s * r * (1 + r)*n) / (12 * ((1 + r)*n - 1))
print(m)
