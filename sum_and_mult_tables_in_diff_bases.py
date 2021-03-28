def convert_number(number: int, system_to: int) -> str:
    """Converts a number into different number system, returns a string."""
    if number == 0:
        return '0'
    if number < 0:
        print('It\'s not possible to convert a number less than 0 now.')
        return 'Error'
    if system_to < 2:
        print('Min provided base is 2.')
        return 'Error'
    if system_to > 36:
        print('Max provided base is 36 due to defined symbols (0-9, A-Z).')
        return 'Error'

    latin_letters = [chr(ord('A') + c) for c in range(0, 26)]
    # small_greek_letters = [chr(code) for code in range(945, 970)]

    result = ''
    while number:
        quotient, remainder = divmod(number, system_to)
        if remainder > 9:
            remainder = latin_letters[remainder - 10]
        result += str(remainder)
        number = quotient
    return result[-1::-1]


def generate_multiplication_table(base: int) -> str:
    """Generates a multiplication table based on given number system."""
    table = ''
    max_len = len(str(base * base))

    # Head line
    table += f''.ljust(max_len + 1, ' ')
    for x in range(1, base):
        table += f'{convert_number(x, base)}'.ljust(max_len + 1, ' ')
    table += '\n'

    # Main content including vertical line
    for x in range(1, base):
        table += f'{convert_number(x, base)}'.ljust(max_len + 1, ' ')
        for y in range(1, base):
            table += f'{convert_number(x * y, base)}'.ljust(max_len + 1, ' ')
        table += '\n'
    return table


def generate_summation_table(base: int) -> str:
    """Generates a summation table based on given number system."""
    table = ''
    max_len = len(str(base * base))

    # Head line
    table += f''.ljust(max_len + 1, ' ')
    for x in range(1, base):
        table += f'{convert_number(x, base)}'.ljust(max_len + 1, ' ')
    table += '\n'

    # Main content including vertical line
    for x in range(1, base):
        table += f'{convert_number(x, base)}'.ljust(max_len + 1, ' ')
        for y in range(1, base):
            table += f'{convert_number(x + y, base)}'.ljust(max_len + 1, ' ')
        table += '\n'
    return table


def main():
    for base in range(2, 17):
        header = f'Таблицы по основанию {base}:'
        sep_line = '=' * len(header)
        print(sep_line, header, sep_line, sep='\n', end='\n\n')
        str_len = len(generate_summation_table(base)) // (base + 1)
        print(f'Таблица сложения'.center(str_len, ' '),
              f'\n{generate_summation_table(base)}')
        print(f'Таблица умножения'.center(str_len, ' '),
              f'\n{generate_multiplication_table(base)}')


if __name__ == '__main__':
    main()
