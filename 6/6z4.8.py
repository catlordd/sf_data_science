
def txt_s(text):
    symbol = text[0]
    result =''
    symbol_i = 0
    i=0
    while True:
        if i >= len(text):
            result = result + symbol + str(symbol_i)
            break
        if symbol == text[i]:
            symbol_i += 1
            i += 1
        else:
            result = result + symbol + str(symbol_i)
            symbol = text[i]
            symbol_i = 0
            
    return result
print(txt_s('aaabbccccdaa'))
