#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    num = 0
    roman_numerals_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number_value = [roman_numerals_dict[x] for x in roman_string] + [0]

    for i in range(len(number_value) - 1):
        if number_value[i] >= number_value[i + 1]:
            num += number_value[i]
        else:
            num -= number_value[i]

    return num
