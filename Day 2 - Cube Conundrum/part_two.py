from typing import List, Tuple

NUM_RED = 12
NUM_GREEN = 13
NUM_BLUE = 14


def load_input() -> List[str]:
    """Load input from file and return as list of strings."""
    ret_str = []
    with open("input.txt") as f:
        for line in f:
            ret_str.append(line.strip())
    return ret_str


def find_number_and_color(input: str) -> Tuple[int, str]:
    """Return the number and color of the cube."""
    colors = ["red", "green", "blue"]
    for color in colors:
        if input.find(color) != -1:
            return int(input[: input.find(color)]), color
    raise ValueError("No color found")


def get_game_power(game: str) -> int:
    max_red_seen = 0
    max_green_seen = 0
    max_blue_seen = 0

    rounds = game.replace(" ", "").split(";")
    for round in rounds:
        cubes_seen = round.split(",")
        for subset in cubes_seen:
            number, color = find_number_and_color(subset)
            if color == "red" and number > max_red_seen:
                max_red_seen = number
            elif color == "green" and number > max_green_seen:
                max_green_seen = number
            elif color == "blue" and number > max_blue_seen:
                max_blue_seen = number
    return max_red_seen * max_green_seen * max_blue_seen


games_log = load_input()
game_set_powers = []
for game in games_log:
    game_set_powers.append(get_game_power(game[game.index(":") + 1 :]))
print(f"Sum of game set powers is: {sum(game_set_powers)}")
