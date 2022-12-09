# Модифицируем предыдущую задачу.
# Теперь необходимо написать функцию get_most_frequent_word, которое возвращает самое часто встречающееся слово в тексте.

punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']

text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

def get_most_frequent_word(text):
    for symb in punctuation_list:
        text = text.replace(symb, '')
    text = text.lower()
    text = list(text.split())

    max_symbol = (text[0], 0)
    for x in text:
        if max_symbol[1] < text.count(x):
            max_symbol = (x, text.count(x))

    return max_symbol
    
print(get_most_frequent_word(text_example))
