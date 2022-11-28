"""
Member #1 Student Name: Alice Hur
Member #1 Student Number: A01272954

Member #2 Student Name: Shuyi Liu
Member #2 Student Number: A01178380
"""

from random import choice


def make_board(rows, columns):
    rooms_coordinates = {}
    rooms_names = ['Empty Room', 'Empty Room', 'Event Room']

    for row in range(rows):
        for col in range(columns):
            coordinate = (row, col)
            if coordinate == (9, 4):
                rooms_coordinates[coordinate] = "Respawn Room"
            else:
                random_room = choice(rooms_names)
                rooms_coordinates[coordinate] = random_room

    return rooms_coordinates


def make_character() -> dict:
    character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Current HP': 10, 'Max HP': 10, 'Age': 5,
                 'Name': input("Enter a character name: ")}
    while True:
        character_gender = input("Choose the gender of your character (M / F): ").upper()
        if character_gender not in ('M', 'F'):
            print("Please enter 'M' for Male, or 'F' for Female.")
        else:
            character['Gender'] = character_gender
            break

    return character


def describe_current_location(board, character):
    current_character_coordinate = (character['X-coordinate'], character['Y-coordinate'])
    current_location = board[current_character_coordinate]

    for _ in range(20):
        print("-", end=" ")
    print()
    for row in range(10):
        for col in range(10):
            if (row, col) == current_character_coordinate:
                print("|\033[92mX\033[00m|", end=" ")
            elif board[(row, col)] == "Respawn Room":
                print("|\033[95mO\033[00m|", end=" ")
            elif board[(row, col)] == "Event Room":
                print("|\033[93m!\033[00m|", end=" ")
            else:
                print("|-|", end=" ")
        print()
    for _ in range(20):
        print("-", end=" ")


def get_user_choice():
    pass


def validate_move(board, character, direction):
    pass


def move_character(character, direction):
    pass


def check_for_challenges(board, character):
    pass


def execute_challenge_protocol(board, character):
    pass


def character_has_leveled(character):
    pass


def execute_glow_up_protocol():
    pass


def check_if_goal_attained(board, character):
    pass


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    while not achieved_goal:
        # Tell the user where they are
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges(board, character)
            if there_is_a_challenge:
                execute_challenge_protocol(board, character)
                if character_has_leveled(character):
                    execute_glow_up_protocol()
            achieved_goal = check_if_goal_attained(board, character)
        else:
            achieved_goal = True


def main():
    # game()
    character = make_character()
    board = make_board(10, 10)
    describe_current_location(board, character)


if __name__ == "__main__":
    main()
