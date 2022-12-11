# Напишите функцию is_divided_by_six(), которая проверяет, делится ли число на шесть. 
# При решении воспользуйтесь тернарным оператором!

# Функция должна вернуть True, если число делится на шесть или False в обратном случае.

# Подсказка: число делится на шесть, если оно делится на 2 и на 3

def is_divided_by_six(number):
    if number % 6 == 0:
        number = True
    else: number = False
    return number

print(is_divided_by_six(13))
print(is_divided_by_six(12))
