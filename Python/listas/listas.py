#Exercise 1
print("\nExercise 1!")
names = ["Jaqueline", "Julia", "Guilherme"]
print(names, "\n")

#Exercise 2
print("\nExercise 2!")
fruits = ["maça", "limao", "abacaxi"]
sugar = ["brigadeiro", "paçoca", "Chocolate"]
feijoada = ["feijao", "linguiça", "farofa"]
print(f"{fruits}\n{sugar}\n{feijoada}")

listona = [fruits, sugar, feijoada]
print(listona)

#Exercise 3
print("\nExercise 3!")

del listona
print("Done!")

#Exercise 4
print("\nExercise 4!")

mercado = ["brigadeiro", "paçoca", "Produtos de limpeza"]
icecream = ["gelado de chocolate", "gelado de paçoca", "gelado de limão"]
print(f"{mercado}\n{icecream}")
mercado.remove("Produtos de limpeza")
icecream.remove("gelado de paçoca")
print(f"{mercado}\n{icecream}")


#Exercise 5
print("\nExercise 5!")

sort_int = [4, 2, 92, 6]
print(sort_int, "\n")
sort_int.sort()
print(sort_int)
reverse = sort_int[::-1]
print(reverse)