# Напишите функцию def even_numbers_in_matrix(), 
# которая получает на вход матрицу (список из списков) 
# и возвращает количество четных чисел в ней.

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]

def even_numbers_in_matrix(matrix):
    result = 0
    for x in matrix:
        for y in x:
            if y%2 == 0: result += 1 
    return result

print(even_numbers_in_matrix(matrix_example))
