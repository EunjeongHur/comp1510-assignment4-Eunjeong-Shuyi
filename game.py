"""
Member #1 Student Name: Alice Hur
Member #1 Student Number: A01272954

Member #2 Student Name: Shuyi Liu
Member #2 Student Number: A01178380
"""

from random import choice, shuffle
import json
from time import sleep


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
                 'Nero': [1, 10], 'Lulu': [1, 10], 'Noah': [1, 10], 'Penelope': [1, 10],
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
    current_character_coordinate = (character['X-coordinate'], character['Y-coordinate'])
    room = board[current_character_coordinate]
    if room == "Empty Room":
        return False
    else:
        return True


def pick_random_character():
    # check if any character relationship score is over 16
    # Otherwise, pick random event character
    # We need to add other characters here
    event_options = ['Nero']

    return choice(event_options)


def execute_challenge_protocol(board, character):
    file = open("./character.json")
    data = json.load(file)
    event_option = pick_random_character()
    event = ""

    for line in data[event_option]:
        if line['episode'] == character[event_option][0]:
            event = line

    get_event(event, character, event_option)
    current_character_coordinate = (character['X-coordinate'], character['Y-coordinate'])
    board[current_character_coordinate] = "Empty room"


def get_event(event, character, other_character_name):
    episode = character[other_character_name][0]
    character_points = character[other_character_name][1]

    gain_or_not = display_script(event, character)

    if gain_or_not:
        character[other_character_name][1] = character_points + event["gain_points"]
    else:
        character[other_character_name][1] = character_points - event["gain_points"]

    character[other_character_name][0] = episode + 1
    print(f'{other_character_name} score: {character[other_character_name][1]}')


def replace_mc_name(name: str, lines: list) -> list:
    replaced_lines = [line.replace("/mc_name", f'\033[92m{name}\033[00m') for line in lines]

    return replaced_lines


def display_script(event, character):
    name = character['Name']
    options = []
    numbers = []
    user_answer = ""

    script = replace_mc_name(name, event["script"])
    gain_points_option_script = replace_mc_name(name, event["gain_points_option_script"])
    no_gain_points_options_script = replace_mc_name(name, event["no_gain_points_options_script"])
    gain_points_option = event["gain_points_option"]
    no_gain_points_options = event["no_gain_points_options"]

    options.append(gain_points_option)
    for option in no_gain_points_options:
        options.append(option)
    shuffle(options)

    for line in script:
        print(f'{line}\n')
        sleep(1.5)

    for number, option in enumerate(options, 1):
        print(f'{number}. {option}')
        numbers.append(str(number))

    while user_answer not in numbers:
        user_answer = input("Choose a number: ")
    print(". . .")
    sleep(1.5)

    if int(user_answer) == options.index(gain_points_option) + 1:
        for script in gain_points_option_script:
            print(f'{script}\n')
            sleep(2)
        return True
    else:
        for script in no_gain_points_options_script:
            print(script)
            sleep(2)
        return False


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
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges(board, character)
            print(there_is_a_challenge)
            if there_is_a_challenge:
                execute_challenge_protocol(board, character)
                if character_has_leveled(character):
                    execute_glow_up_protocol()
            # achieved_goal = check_if_goal_attained(board, character)
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
