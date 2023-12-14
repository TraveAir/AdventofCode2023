from typing import List, Tuple


def load_input() -> List[str]:
    """Load input from file and return as list of strings."""
    ret_str = []
    with open("input.txt") as f:
        for line in f:
            ret_str.append(line.strip())
    return ret_str


def find_digits(input_str: str) -> Tuple[int, int]:
    """Return the first and last digit in the input string"""
    # Find first digit
    for i in range(len(input_str)):
        if input_str[i].isdigit():
            first_digit = int(input_str[i])
            break

    # Find last digit
    for i in range(len(input_str) - 1, -1, -1):
        if input_str[i].isdigit():
            last_digit = int(input_str[i])
            break
    return first_digit, last_digit


def combine_digits(digits: Tuple[int, int]) -> int:
    """Combine the two digits into a single number"""
    string = f"{digits[0]}{digits[1]}"
    return int(string)


calibration_input = load_input()
calibration_numbers = []
for line in calibration_input:
    digits = find_digits(line)
    calibration_numbers.append(combine_digits(digits))
calibration_sum = sum(calibration_numbers)
print(f"Sum is: {calibration_sum}")
