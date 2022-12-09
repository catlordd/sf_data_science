# Числа Фибоначчи. 

# Напишите функцию def fib_number(), которая получается на вход некоторое 
# число n и выводит n-e число Фибоначчи. 
# Задачу можно решить как с помощью цикла for, так и с помощью цикла while

# Примечание: числа Фибоначчи определяются так


# ```
# a0 = 0, a1 = 1, a2 = a1 + a0 = 1, an = a_n-1 + a_n-2
# ```

# Примечание: в модуле по функциям уже было задание на вычисление чисел Фибоначчи 
# с помощью рекурсивных функций. Здесь необходимо реализовать те же вычисления, 
# но без использования рекурсии.

def fib_number(n):
    if n == 1 or n == 0:
        n = 1
        return n

    return fib_number(n-1) + fib_number(n-2)

print(fib_number(0))
print(fib_number(1))
print(fib_number(2))