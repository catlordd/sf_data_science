# Разработайте функцию holes_count(), которая подсчитывает количество отверстий 
# в заданном числе. Например, в цифре 8 два отверстия, в цифре 9 - одно. 
# В числе 146 - два отверстия. 
# Подсказка: используйте словарь для записи количества отверстий в цифрах

def holes_count(number):
    number = str(number)
    
    result = 0
    for x in number:
        x = int(x)
        if x == 0 or x == 4 or x == 6 or x == 9:
            result += 1
        elif x == 8:
            result += 2
    return result

print(holes_count(123))
print(holes_count(8888))
