from translate import (
    char_to_morse,
    morse_to_char
)

modes = {
    1: char_to_morse,
    2: morse_to_char
}


def main():
    mode = int(input("""
    1. Encode
    2. Decode
    ----------
    Mode: """))
    content = input("""
    Write here: """)
    print(modes[mode](content))


if __name__ == '__main__':
    main()
