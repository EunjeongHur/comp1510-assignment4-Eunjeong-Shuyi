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
    rooms_names = ['Empty Room', 'Empty Room', 'Empty Room', 'Empty Room', 'Empty Room', 'Event Room']

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
    character = {'X-coordinate': 9, 'Y-coordinate': 4,
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
            print(f'{direction}:{value}', end=" ")

        user_choice = input("\nPlease enter a Number corresponding to the direction you wish to travel:\n")
        if user_choice.lower() == "q" or user_choice.lower() == "quit":
            break
        elif user_choice in numbers:
            return directions[int(user_choice) - 1]
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
    print(room)
    if room == "Empty Room" or room == "Respawn Room":
        print('no event here')
        return False
    else:
        return True


def check_route(character):
    # check if character chooses home route or wild route
    if character['Penelope'][1] >= 15:
        print('You are in home route now')
        # we can remove this print statement later
        return True
    else:
        print("You are in wild route now")
        return False


def pick_random_character(character):
    is_home_route = check_route(character)
    # print(character)
    if is_home_route:
        return 'Penelope'
    else:
        return event_option(character)


def event_option(character):
    print(character)
    event_options = ['Nero', 'Lulu', 'Noah', 'Penelope']
    if character['Penelope'][0] == 1:
        return choice(event_options)
    else:
        return check_if_score_reached(character)


def check_if_score_reached(character):
    if character['Nero'][0] == 4 and character['Nero'][1] >= 15:
        return 'Nero'
    elif character['Lulu'][0] == 5 and character['Lulu'][1] >= 15:
        return 'Lulu'
    elif character['Noah'][0] == 5 and character['Noah'][1] >= 15:
        return 'Noah'
    else:
        result = check_if_game_ended(character)
        if len(result) == 0:
            return "ending"
        else:
            return choice(result)


def check_if_game_ended(character):
    other_characters = ['Nero', 'Lulu', 'Noah']
    removed_characters = []

    for char in range(len(other_characters)):
        if character[other_characters[char]][0] >= 4 and character[other_characters[char]][1] < 15:
            removed_characters.append(other_characters[char])
        elif character[other_characters[char]][0] > 4 and character[other_characters[char]][1] >= 20:
            removed_characters.append(other_characters[char])
        else:
            continue
    for char in removed_characters:
        other_characters.remove(char)

    return other_characters


def execute_challenge_protocol(board, character):
    print(event_option)
    file = open("./character.json")
    data = json.load(file)
    event_character = pick_random_character(character)
    if event_option == "ending":
        return True
    else:
        event = ""

        for line in data[event_character]:
            if line['episode'] == character[event_character][0]:
                event = line
        print(f'---{event_option} Event---\n')
        get_event(event, character, event_character)
        current_character_coordinate = (character['X-coordinate'], character['Y-coordinate'])
        board[current_character_coordinate] = "Empty Room"


def display_ending_script():
    # firstly, check how the mc ends the game.
    #
    # if MC reaches Happy ending for core event?
    # print("happy ending")
    # if MC got bad ending for core event?
    # print("bad ending")
    # if MC didn't get to core event?
    # print("You couldn't reach over 15 relationship score for each of the characters")  # something like this
    print("This is the end of a cat's story.")


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
        # sleep(1.5)

    for number, option in enumerate(options, 1):
        print(f'{number}. {option}')
        numbers.append(str(number))

    while user_answer not in numbers:
        user_answer = input("Choose a number: ")
    print(". . .")
    # sleep(1.5)

    if int(user_answer) == options.index(gain_points_option) + 1:
        for script in gain_points_option_script:
            print(f'{script}\n')
            # sleep(2)
        return True
    else:
        for script in no_gain_points_options_script:
            print(script)
            # sleep(2)
        return False


def character_has_leveled(character):
    pass


def execute_glow_up_protocol():
    pass


def check_if_goal_attained(character):
    # check if mc reaches the end of events
    if character['Nero'][0] == 5:
        return True
    elif character['Lulu'][0] == 6:
        return True
    elif character['Noah'][0] == 6:
        return True
    elif character['Penelope'][0] == 5:
        return True
    else:
        return False


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
        # if direction is False:
        #     achieved_goal = True
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            there_is_a_challenge = check_for_challenges(board, character)
            # print(there_is_a_challenge)
            if there_is_a_challenge:
                achieved_goal = execute_challenge_protocol(board, character)
                if check_if_goal_attained(character):
                    achieved_goal = True
                # if character_has_leveled(character):
                #     execute_glow_up_protocol()
            # achieved_goal = check_if_goal_attained(board, character)
        else:
            print("You can't go that direction!")
            get_user_choice()
    display_ending_script()


def main():
    game()
    # character = make_character()
    # board = make_board(10, 10)
    # describe_current_location(board, character)
    # direction = get_user_choice()
    # print(direction)


if __name__ == "__main__":
    main()
