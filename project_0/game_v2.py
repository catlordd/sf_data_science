import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданое число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    max_number = 100 # Максимальное значение для бинарный поиска
    min_number = 0 # Минимальное значение для бинарный поиск
    predict_number = int(max_number+min_number) / 2

    while True:
        count += 1
        #predict_number = np.random.randint(1, 101) # предполагаемое число
        # Алгоритм бинарный поиска
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number > predict_number:
            if min_number == predict_number and min_number == 99:
                break # выход из цикла, если угадали 
            min_number = predict_number 
        elif number < predict_number:
            max_number = predict_number
        predict_number = int((max_number+min_number) / 2)
        
    return(count)

#print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


# RUN
if __name__ == '__main__':
    print(score_game(random_predict))
