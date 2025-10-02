def roman_to_int(s: str) -> int:
    """
    Converts a Roman numeral string to an integer.

    Args:
      s: The Roman numeral string.

    Returns:
      The integer representation.
    """
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = roman_map[s[-1]]

    for i in range(len(s) - 2, -1, -1):
        current_val = roman_map[s[i]]
        next_val = roman_map[s[i + 1]]

        if current_val < next_val:
            total -= current_val
        else:

            total += current_val
            

    return total


print(f"Input: 'III', Output: {roman_to_int('III')}")
print(f"Input: 'LVIII', Output: {roman_to_int('LVIII')}")
print(f"Input: 'MCMXCIV', Output: {roman_to_int('MCMXCIV')}")