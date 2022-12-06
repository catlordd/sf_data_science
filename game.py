import numpy as np

numder = np.random.randint(1, 100) # it's propose number
count = 0 # count tries

while True:
    count += 1
    predict_number = int(input('Predict number! Your number is : ')) # it's intering number
    
    if predict_number > numder:
        print("Чисто должно быть меньше")
    elif predict_number < numder:
        print("Чисто должно быть больше")
    else:
        print(f"Вы угадали число! Это: {numder}. Число затраченных попыток: {count}")
        break
    
