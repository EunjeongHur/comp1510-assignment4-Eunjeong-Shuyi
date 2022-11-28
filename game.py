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
    print()


def get_user_choice():
    directions = ['Up', 'Down', 'Left', 'Right']
    numbers = ['1', '2', '3', '4']
    print("To quit a game, type 'q' or 'quit'\n")

    while True:
        for value, direction in enumerate(directions, 1):
            print(f'{value}.{direction}', end=" ")

        user_choice = input("\nPlease enter a Number corresponding to the direction you wish to travel:\n")
        if user_choice.lower() == "q" or user_choice.lower() == "quit":
            break
        elif user_choice in numbers:
            return directions[int(user_choice)-1]
        else:
            continue

    return False


def validate_move(character, direction):
    current_character_coordinate = (character['X-coordinate'], character['Y-coordinate'])

    if current_character_coordinate[0] == 0 and direction == 'Up':
        return False
    elif current_character_coordinate[0] == 9 and direction == 'Down':
        return False
    elif current_character_coordinate[1] == 0 and direction == 'Left':
        return False
    elif current_character_coordinate[1] == 9 and direction == 'Right':
        return False
    else:
        return True


def move_character(character, direction):
    current_x_location = character['X-coordinate']
    current_y_location = character['Y-coordinate']

    if direction == 'Up':
        character['X-coordinate'] = current_x_location - 1
    elif direction == 'Down':
        character['X-coordinate'] = current_x_location + 1
    elif direction == 'Left':
        character['Y-coordinate'] = current_y_location - 1
    else:
        character['Y-coordinate'] = current_y_location + 1


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
        if direction is False:
            achieved_goal = True
        valid_move = validate_move(character, direction)
        print(valid_move)
        if valid_move:
            move_character(character, direction)
        #     describe_current_location(board, character)
        #     there_is_a_challenge = check_for_challenges(board, character)
        #     if there_is_a_challenge:
        #         execute_challenge_protocol(board, character)
        #         if character_has_leveled(character):
        #             execute_glow_up_protocol()
        #     achieved_goal = check_if_goal_attained(board, character)
        else:
            achieved_goal = True


def main():
    game()
    # character = make_character()
    # board = make_board(10, 10)
    # describe_current_location(board, character)
    # direction = get_user_choice()
    # print(direction)


if __name__ == "__main__":
    main()
