from typing import List, Tuple
import math


def load_input() -> List[str]:
    """Load input from file and return as list of strings."""
    ret_str = []
    with open("input.txt") as f:
        for line in f:
            ret_str.append(line.strip())
    return ret_str


def convert_to_int(input_str: str) -> int:
    """Convert the input string to an integer"""
    if input_str.isdigit():
        return int(input_str)
    else:
        digit_words = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        return digit_words[input_str]


def find_digits(input_line: str) -> Tuple[int, int]:
    """Return the first and last digit in the input string"""

    digit_words = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    min = math.inf
    max = -math.inf
    for i in range(len(input_line)):
        substrings = [
            input_line[i],
            input_line[i : i + 3],
            input_line[i : i + 4],
            input_line[i : i + 5],
        ]
        for substr in substrings:
            if substr in digit_words or substr.isdigit():
                if i < min:
                    min = i
                    first_digit = convert_to_int(substr)
                if i > max:
                    max = i
                    last_digit = convert_to_int(substr)
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
