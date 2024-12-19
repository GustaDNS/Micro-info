#exercise 1
print("\nExercise 1!")
quote = ("Python é muito legal.")
f = quote[:6]
f1 = quote[0:6]
f2 = quote[9:14]
f3 = quote[15:21]
f4 = quote[7]
print(f"{quote}\n{f}\n{f1}\n{f4}\n{f2}\n{f3}\n")

#exercise 2
print("Exercise 2!")
quote_len = len(quote)
f_len = len(f)
f1_len = len(f1)
f2_len = len(f2)
f3_len = len(f3)
f4_len = len(f4)


print(f"{quote_len}\n{f_len}\n{f1_len}\n{f4_len}\n{f2_len}\n{f3_len}\n")

#exercise 3
print("Exercise 3!")
split_quote = quote.split()
print(split_quote)
len_split_quote = len(split_quote)
len_split_quote1 = len(split_quote[0])
len_split_quote2 = len(split_quote[1])
len_split_quote3 = len(split_quote[2])
len_split_quote4 = len(split_quote[3])
print(len_split_quote)
print(len_split_quote1)
print(len_split_quote2)
print(len_split_quote3)
print(len_split_quote4, "\n")

# exercise 4
print("Exercise 4!")
reversed = quote[::-1]
print(reversed)