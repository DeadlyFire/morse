# Латинский алфавит
MorseCodeEn = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',

    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
    '-..-': 'X', '-.--': 'Y', '--..': 'Z',
}

# Кириллица
MorseCodeRu = {
    "А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..", "Е": ".",
    "Ё": ".", "Ж": "...-", "З": "--..", "И": "..", "Й": ".---", "К": "-.-",
    "Л": ".-..", "М": "--", "Н": "-.", "О": "---", "П": ".--.", "Р": ".-.",
    "С": "...", "Т": "-", "У": "..-", "Ф": "..-.", "Х": "....", "Ц": "-.-.",
    "Ч": "---.", "Ш": "----", "Щ": "--.-", "Ъ": ".--.-.", "Ы": "-.--", "Ь": "-..-",
    "Э": "..-..", "Ю": "..--", "Я": ".-.-",

    ".-": "А", "-...": "Б", ".--": "В", "--.": "Г", "-..": "Д",
    ".": "Е", "...-": "Ж", "--..": "З", "..": "И", ".---": "Й", "-.-": "К",
    ".-..": "Л", "--": "М", "-.": "Н", "---": "О", ".--.": "П", ".-.": "Р",
    "...": "С", "-": "Т", "..-": "У", "..-.": "Ф", "....": "Х", "-.-.": "Ц",
    "---.": "Ч", "----": "Ш", "--.-": "Щ", ".--.-.": "Ъ", "-.--": "Ы", "-..-": "Ь",
    "..-..": "Э", "..--": "Ю", ".-.-": "Я"
}

# Цифры
MorseCodeNu = {
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": "/",

    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", "/": " "
}

language = None


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


# Основная программа
def main():
    global language
    text = None
    print('Здравствуйте! Пожалуйста, выберите язык программы.',
          'Напишите “Ru” — если Ваш язык русский или “En” — если английский.', '',
          'Hello! Please select the language of the program.',
          'Write “Ru” if your language is Russian or “En” if it is English.', sep='\n')

    # Проверка, чтобы пользователь точно выбрал язык
    while language != 'Ru' and language != 'En':
        language = input()
        if language != 'Ru' and language != 'En':
            print('Извините, не понял Вас. Попробуйте еще раз.',
                  "I'm sorry, I didn't understand you. Try again.", sep='\n')

    # Разделение программы по языкам на 2 подпрограммы
    if language == 'Ru':
        print('Добро пожаловать в “Переводчик текста в морзянку”!',
              'Нажмите “ENTER”, когда захотите остановить программу.', sep='\n')
        while text != "":
            print('Выберите операцию: “Закодировать” текст или “Раскодировать” текст.')
            text = input()
            if text == 'Закодировать' or text == 'закодировать':
                encode_to_morse(input('Введите текст: ').upper())
                print()
            elif text == 'Раскодировать' or text == 'раскодировать':
                decode_from_morse(input('Введите текст: ').upper())
                print()
            elif text != '':
                print('Извините, не понял Вас. Попробуйте еще раз.')

    else:
        print('Welcome to “Text to Morse Language Translator”!',
              'Press “ENTER” when you want to stop the program.', sep='\n')
        while text != "":
            print('Select operation: “Encode” text or “Decode” text.')
            text = input()
            if text == 'Encode' or text == 'encode':
                encode_to_morse(input('Enter the text: ').upper())
                print()
            elif text == 'Decode' or text == 'decode':
                decode_from_morse(input('Enter the text: ').upper())
                print()
            elif text != '':
                print("I'm sorry, I didn't understand you. Try again.")