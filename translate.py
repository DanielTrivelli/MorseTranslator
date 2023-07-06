from scripts.morse_code import MORSE_CODE, INVERTED_MORSE_CODE


def char_to_morse(chars: str) -> str:
    return ''.join([
        MORSE_CODE[char] + ' ' if char in MORSE_CODE else '  ' for char in chars.lower()
    ])


def morse_to_char(morse: str) -> str:
    return ''.join([
        INVERTED_MORSE_CODE[char] if char in INVERTED_MORSE_CODE else ' ' for char in morse.split(' ')
    ])
