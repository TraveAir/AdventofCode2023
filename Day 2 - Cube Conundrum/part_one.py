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


def game_is_possible(game: str) -> bool:
    rounds = game.replace(" ", "").split(";")
    for round in rounds:
        cubes_seen = round.split(",")
        for subset in cubes_seen:
            number, color = find_number_and_color(subset)
            if color == "red" and number > NUM_RED:
                return False
            elif color == "green" and number > NUM_GREEN:
                return False
            elif color == "blue" and number > NUM_BLUE:
                return False
    return True


games_log = load_input()
possible_game_ids = []
for game in games_log:
    game_number = int(game[5 : game.index(":")])
    if game_is_possible(game[game.index(":") + 1 :]):
        possible_game_ids.append(game_number)
print(f"Sum of possible game IDs: {sum(possible_game_ids)}")
