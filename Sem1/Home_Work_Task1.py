# Найдите сумму цифр трехзначного числа n
# Результат сохраните в переменную res

n = int(input("Введите трехзначное число: "))

# a = n // 100
# b = (n % 100) // 10
# c = n % 10
# res = a + b + c
# print(f"n =", n, "-> res = ", res, "(", a, "+", b, "+", c, ")")

# res = n // 100 + (n % 100) // 10 + n % 10
# print(f"n =", n, "-> res = ", res, "(", n // 100, "+", (n % 100) // 10, "+", n % 10, ")")

# res = 0
# while n > 0:
#     a = n % 10                      # а = 321 % 10 = 1       a = 32 % 10 = 2        a = 3 % 10 = 3 
#     res += a               # res = res + 1 = 0 + 1 = 1       res = 1 + 2 = 3        res = 3 + 3 = 6
#     n //= 10            # n = n // 10 = 321 // 10 = 32       n = 32 // 10 = 3       n = 3 // 10 = 0
# print(res)

res = 0
for a in str(n):   # для а в строке 231     Внутри цикла мы преобразуем каждую цифру обратно в целое число
    res += int(a)  # res = 0 + число(а)     с помощью функции int() и добавляем его к сумме цифр res.
print(res)