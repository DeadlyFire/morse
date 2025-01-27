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