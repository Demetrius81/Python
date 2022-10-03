x = '.... . -.--   .--- ..- -.. .'
y = "ЭЙ, ДЖУД"


def createCodeDict() -> dict:
    code = {'A': '.-', 'B': '-...', 'C': '-.-.',
            'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----',
            '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', '0': '-----'}
    return code


def createSymDict() -> dict:
    sym = {'.-': 'A', '-...': 'B', '-..': 'D',
           '-.-.': 'C', '.': 'E', '..-.': 'F',
           '--.': 'G', '....': 'H', '..': 'I',
           '.---': 'J', '-.-': 'K', '.-..': 'L',
           '--': 'M', '-.': 'N', '---': 'O',
           '.--.': 'P', '--.-': 'Q', '.-.': 'R',
           '...': 'S', '-': 'T', '..-': 'U',
           '...-': 'V', '.--': 'W', '-..-': 'X',
           '-.--': 'Y', '--..': 'Z', '.----': '1',
           '..---': '2', '...--': '3', '....-': '4',
           '.....': '5', '-....': '6', '--...': '7',
           '---..': '8', '----.': '9', '-----': '0',
           '*': ' '}
    return sym


MORSE_CODE = createSymDict()


def decode_morse(morse_code):
    code = createSymDict()
    f = []
    for i in morse_code.replace('   ', ' * ').split(' '):
        f.append(code[i])
    return ''.join(f).encode('ascii')


    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')


a = decode_morse(x)
print(a)
