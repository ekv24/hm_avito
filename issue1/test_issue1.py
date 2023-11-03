LETTER_TO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": " ",
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> encode('123')
    '.---- ..--- ...--'
    >>> encode('HELLO WORLD')
    '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
    >>> encode(')?/')
    '-.--.- ..--.. -..-.'
    >>> encode('BAAAB') # doctest: +ELLIPSIS
    '-... .- ... -...'
    >>> encode('111')
    '.----          .----           .----'
    >>> encode('SOS')
    '... --- ...'
    >>> encode('hello')
    Traceback (most recent call last):
    ...
    ValueError: принимаются только заглавные буквы
    """
    for symbol in message:
        if symbol != symbol.upper():
            raise ValueError("принимаются только заглавные буквы")

    encoded_signs = [LETTER_TO_MORSE[letter] for letter in message]

    return " ".join(encoded_signs)


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
