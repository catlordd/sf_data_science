# Напишите функцию def matrix_sum(), которая получает на вход две матрицы 
# и возвращает их сумму.

# Примечание: чтобы найти сумму двух матриц, нужно просуммировать 
# их соответствующие элементы. Но перед этим необходимо проверить, что размеры 
# матриц одинаковы (одинаковое количество столбцов и одинаковое количество строк)

# Например:

# 1 2 3   2 3 4   3 5 7
# 2 3 4 + 4 5 6 = 6 8 10
# 5 6 7   4 3 2   9 9 9

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]

def matrix_sum(matrix1, matrix2):
    result =[]
    if len(matrix1) != len(matrix1):
        print('Error! Matrices dimensions are different!')
        return None
    i = 0
    for m1, m2 in zip(matrix1, matrix2):
        if len(m1) != len(m2):
            print('Error! Matrices dimensions are different!')
            return None
        result.append([])
        
        for x1, x2 in zip(m1 ,m2):
            result[i].append (x1 + x2)
            print(result)
        i += 1   
          
            
    return result

print(matrix_sum(matrix_example, matrix_example))
