# Функция раскодирования
def decode_from_morse(code: str):
    decode_cod = ""
    code = code.split()
    if language == "Ru":
        for symbol in code:
            decode_cod += MorseCodeNu.get(symbol, "")
            decode_cod += MorseCodeRu.get(symbol, "")
    else:
        for symbol in code:
            decode_cod += MorseCodeNu.get(symbol, "")
            decode_cod += MorseCodeEn.get(symbol, "")
    print(decode_cod.capitalize())


#  Функция кодирования
def encode_to_morse(text: str):
    my_list = []
    for i in text:
        my_list.append(MorseCodeRu.get(i))
        my_list.append(MorseCodeEn.get(i))
        my_list.append(MorseCodeNu.get(i))
    print(' '.join([i for i in my_list if i is not None]))