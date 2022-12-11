# Напишите функцию lucky_ticket(), которая проверяет, является ли билетик счастливым.

# Памятка: билетик счастливый, если сумма первых трех цифр равна сумме последних трех цифр.

# На вход функция получает шестизначное число.

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    first_n = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    last_n = int(ticket_number[-1]) + int(ticket_number[-2]) + int(ticket_number[-3])
    return first_n == last_n

print(lucky_ticket(111111))
print(lucky_ticket(123456))
