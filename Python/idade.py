age = int(input("Qual é sua idade? "))
year = 2024 - age
print("Você nasceu em:", year)


age_test = int(input("Qual é sua idade? "))
year_test = int(input("Em que ano você nasceu? "))

if 2024 - year_test == age_test:
    print("Você já fez anos!")
else:
    print("Você não fez anos!")

fahrenheit = int(input("Qual é a temperatura em F? "))

celsius = (fahrenheit - 32) / 1.8
print("A coversão de fahreinheit para celsius é: ", str(celsius) + "ºC")