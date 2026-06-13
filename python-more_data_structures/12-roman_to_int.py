#!/usr/bin/python3

def roman_to_int(roman_string):
    # 1. Guard Rail: Check if it's missing, None, or not a string
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    length = len(roman_string)
    # 2. Loop through the string by its index positions
    for i in range(length):
        current_value = roman_dict.get(roman_string[i], 0)
        # Check if there is a next numeral, and look at its value
        if i + 1 < length:
            next_value = roman_dict.get(roman_string[i + 1], 0)
        else:
            next_value = 0
        # 3. Subtraction Rule vs Addition Rule
        if current_value < next_value:
            total -= current_value  # Subtract if a larger value follows
        else:
            total += current_value  # Otherwise, add it normally
    return total
