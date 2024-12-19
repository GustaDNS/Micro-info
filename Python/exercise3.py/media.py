nbr1 = int(input("Digite um número: "))
nbr2 = int(input("Digite um número: "))
nbr3 = int(input("Digite um número: "))
nbr4 = int(input("Digite um número: "))
x = (nbr1 + nbr2 + nbr3 + nbr4) / 4

if (nbr1 or nbr2 or nbr3 or nbr4) > 0:
	print(f"A média de {nbr1}, {nbr2}, {nbr3}, {nbr4} é: {x}")
else:
	print("Um dos números anteriores não é positivo!")