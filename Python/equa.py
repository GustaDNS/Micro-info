import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"A equação tem uma raiz real: x = {x}")
else:
    print("A equação não tem raízes reais.")