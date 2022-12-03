"""
Member #1 Student Name: Alice Hur
Member #1 Student Number: A01272954

Member #2 Student Name: Shuyi Liu
Member #2 Student Number: A01178380
"""

from random import choice, shuffle
from time import sleep
import json
import ascii_art


def make_board(rows: int, columns: int) -> dict:
    """
    Make board to show game map to users.

    :param rows: an integer that is in range [1, 10] inclusive
    :param columns: an integer that is in range [1, 10] inclusive
    :precondition: rows and columns must be integers that are in range [1, 10] inclusive
    :postcondition: generate the board that shows game map to users
    :postcondition: generate a 10*10 board
    :return: the board that shows game map to users as a dictionary
    """
    rooms_coordinates = {}
    rooms_names = ['Empty Room', 'Empty Room', 'Empty Room', 'Empty Room', 'Event Room']

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
    """
    Generate a character with all attributes and input username.

    :precondition: input for character must be a non-empty string
    :precondition: input for character gender be a "F" or "M"
    :postcondition: ask user to re-enter inputs if inputs are not valid
    :postcondition: generate a character with all attributes and input username and input gender
    :return: generate a character with all attributes and input username as a dictionary
    """
    character = {'X-coordinate': 9, 'Y-coordinate': 4,
                 'Nero': [1, 10], 'Lulu': [1, 10], 'Noah': [1, 10], 'Penelope': [1, 10],
                 'Name': input("Enter a character name: ")}
    if character['Name'].strip() == "":
        print("Please enter a non-empty character name")
        make_character()
    else:
        while True:
            character_gender = input("Choose the gender of your character (M / F): ").upper()
            if character_gender not in ('M', 'F'):
                print("Please enter 'M' for Male, or 'F' for Female.")
            else:
                character['Gender'] = character_gender
                break
        display_opening(character)
        return character


def display_opening(character: dict):
    """
    Display the opening script after a character is made.

    :param character: a dictionary
    :precondition: character must be a dictionary
    :postcondition: display the opening script after a character is made
    """
    print("\nCharacter is successfully created!")
    sleep(0.5)
    print("\nYou woke up from your dream and started grooming yourself.")
    sleep(1.5)
    print(f"\nYour name is {character['Name']}, and you are a stray cat in Vancouver.\n")
    sleep(1.5)
    ascii_art.city_art()
    sleep(2)
    print("\nAfter grooming yourself, you stood up and was ready to start your new day of adventure.\n")
    sleep(3)
    ascii_art.a_cats_story()
    sleep(2)
    print("\nStart your adventure by entering '1','2','3','4'")
    sleep(2)


def describe_current_location(board: dict, character: dict):
    """
    Generate an updated map board after character moves.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board and character must be dictionaries
    :postcondition: generate an updated map board after character moves
    """
    current_character_coordinate = (character['X-coordinate'], character['Y-coordinate'])

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


def get_user_choice() -> bool or str:
    """
    Get user's input for moving and reflect as direction or allow user quit the game.

    :precondition: user must enter '1', '2', '3', '4' to move
    :precondition: user must enter 'q' or 'quit' (case-insensitive) to move
    :postcondition: user can move 'Up', 'Down', 'Left', 'Right' by entering '1', '2', '3', '4'
    :postcondition: end the game if user types 'q' or 'quit' (case-insensitive)
    :return: direction that user choose to move as a string or False if when user types 'q' or 'quit'
    """
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


def validate_move(character: dict, direction: str) -> bool:
    """
    Determine if move is validate.

    :param character: a dictionary
    :param direction: a string
    :precondition: character must be a dictionary
    :precondition: direction must be a string that is one of 'Up', 'Down', 'Left', 'Right'
    :postcondition: determine if move is validate
    :postcondition: invalidate move if character reaches boarders of the map
    :return: True if move is validate, False if not

    >>> test_character = {'X-coordinate': 3, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10], \
    'Penelope': [1, 10], 'Name': 'Shuyi'}
    >>> test_direction = 'Down'
    >>> validate_move(test_character, test_direction)
    True
    >>> test_character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10], \
    'Penelope': [1, 10], 'Name': 'Shuyi'}
    >>> test_direction = 'Down'
    >>> validate_move(test_character, test_direction)
    False
    """
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
    """
    Move character to position on the map based on where character's current position and direction it moves.

    :param direction:
    :param character: a dictionary
    :precondition: character must be a dictionary
    :precondition: direction must be a string that is one of 'Up', 'Down', 'Left', 'Right'
    :postcondition: change character's X-coordinate and Y-coordinate based on direction
    >>> my_character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], \
    'Noah': [1, 10], 'Penelope': [1, 10], 'Name': 'Chris'}
    >>> my_direction = 'Up'
    >>> move_character(my_character, my_direction)
    >>> my_character['X-coordinate']
    8
    >>> my_character = {'X-coordinate': 5, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], \
    'Noah': [1, 10], 'Penelope': [1, 10], 'Name': 'Chris'}
    >>> my_direction = 'Down'
    >>> move_character(my_character, my_direction)
    >>> my_character['X-coordinate']
    6
    >>> my_character = {'X-coordinate': 5, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], \
    'Noah': [1, 10], 'Penelope': [1, 10], 'Name': 'Chris'}
    >>> my_direction = 'Left'
    >>> move_character(my_character, my_direction)
    >>> my_character['Y-coordinate']
    3
    >>> my_character = {'X-coordinate': 5, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], \
    'Noah': [1, 10], 'Penelope': [1, 10], 'Name': 'Chris'}
    >>> my_direction = 'Right'
    >>> move_character(my_character, my_direction)
    >>> my_character['Y-coordinate']
    5

    """
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


def check_for_challenges(board: dict, character: dict) -> bool:
    """
    Determine if current location has an event.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must contain rooms coordinate for key and room description for value
    :precondition: character must contain current user's information
    :post condition: 'Empty Room' and 'Respawn Room' are considered as not having events
    :post condition: if current location has event, return True. Otherwise, return False
    :return: return True if current location has event, else return False
    """
    current_character_coordinate = (character['X-coordinate'], character['Y-coordinate'])
    room = board[current_character_coordinate]
    if room == "Empty Room" or room == "Respawn Room":
        print('no event here')
        return False
    else:
        return True


def check_route(character: dict) -> bool:
    """
    Check if user is in Penelope route.

    :param character: a dictionary
    :precondition: character must be a dictionary
    :postcondition: print home route message and return True if user is in Penelope route
    :postcondition: print wild route message and return True if user is not in Penelope route
    :return: True of user is in Penelope route, False if not
    """
    # check if character chooses home route or wild route
    if character['Penelope'][1] >= 15:
        print('You are in home route now')
        # we can remove this print statement later
        return True
    else:
        print("You are in wild route now")
        return False


def pick_random_character(character: dict):
    """
    Select 'Penelope' character if in home route.

    :param character: a dictionary
    :precondition: character must be a dictionary
    :postcondition: select 'Penelope' character if in home route based on output of function check_route
    :return: 'Penelope' as a string or event_option(character) as a function
    """
    is_home_route = check_route(character)
    if is_home_route:
        return 'Penelope'
    else:
        return event_option(character)


def event_option(character: dict):
    """
    Generate next event choice.

    :param character: a dictionary
    :precondition: character must be a dictionary
    :postcondition: select a random element in list event_options if Penelope's script has not been displayed yet
    :postcondition: call function check_if_score_reached if Penelope's first script has already been displayed
    :return: next event choice as a string or check_if_score_reached(character) as a function
    """
    event_options = ['Nero', 'Lulu', 'Noah', 'Penelope']
    if character['Penelope'][0] == 1:
        return choice(event_options)
    else:
        return check_if_score_reached(character)


def check_if_score_reached(character: dict) -> str:
    """
    Check if critical scores are reached and put user into individual route according to scores.

    :param character: a dictionary
    :precondition: character must be a dictionary
    :postcondition: put user into Nero route if 3 nero scripts were displayed and Nero relationship point >= 15
    :postcondition: put user into Lulu route if 4 Lulu scripts were displayed and Lulu relationship point >= 15
    :postcondition: put user into Noah route if 4 Noah scripts were displayed and Noah relationship point >= 15
    :postcondition: display text if relationships from all chars are lower than 15
    :postcondition: put user into ending route if no more character options are available
    :return: next event choice as a string
    """
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


def check_if_game_ended(character: dict) -> list:
    """
    Check if the game has ended.

    :param character: a dictionary
    :precondition: character must be a dictionary
    :postcondition: check if the game has ended based on scripts displayed and relationship scores with characters
    :postcondition: generate a list other_characters for function check_if_score_reached based on scripts
    displayed and relationship scores with characters
    :postcondition: if all non-critical scripts of a character were played and relationship point is lower than 15,
    disable the route so this route will not show up in random choices
    :return: characters that are left saved in other_characters as a list
    """
    other_characters = ['Nero', 'Lulu', 'Noah']
    removed_characters = []

    for char in range(len(other_characters)):
        if character[other_characters[char]][0] >= 4 and character[other_characters[char]][1] < 15:
            removed_characters.append(other_characters[char])
        else:
            continue
    for char in removed_characters:
        other_characters.remove(char)

    return other_characters


def execute_challenge_protocol(board: dict, character: dict):
    """
    Execute the challenge protocol according to event_option output.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary
    :precondition: character must be a dictionary
    :postcondition: Execute the challenge protocol according to event_option output
    :return: True of event_character is "ending"
    """
    file = open("./character.json")
    data = json.load(file)
    event_character = pick_random_character(character)
    if event_character == "ending":
        return True
    else:
        event = ""

        for line in data[event_character]:
            if line['episode'] == character[event_character][0]:
                event = line
        print(f'---{event_character} Event---\n')
        get_event(event, character, event_character)
        current_character_coordinate = (character['X-coordinate'], character['Y-coordinate'])
        board[current_character_coordinate] = "Empty Room"


def display_ending_script(character: dict) -> None:
    """
    Display ascii art and ending scripts.

    :param character: a dictionary
    :precondition: character must be a dictionary containing user's information
    :postcondition: if character completes critical events for any of the character and relationship score is over 20,
    display happy_ending ascii art text and cat of ascii art
    :postcondition: if character completes critical events for any of the character and relationship score is under 20,
    display bad_ending ascii art text and cat of ascii art
    :postcondition: if character doesn't complete any critical events, display ending scripts and
    bad_ending ascii art text and cat of ascii art
    :postcondition: after displaying ascii arts, prints ending credits
    """
    if character['Nero'][0] == 5 or character['Lulu'][0] == 6:
        if character['Nero'][1] >= 20 or character['Lulu'][1] >= 20:
            ascii_art.happy_ending()
            ascii_art.two_cats_art()
        else:
            ascii_art.bad_ending()
            ascii_art.lonely_cat_art()
    elif character['Noah'][0] == 6:
        if character['Noah'][1] >= 20:
            ascii_art.happy_ending()
            ascii_art.sleeping_cat_art()
        else:
            ascii_art.bad_ending()
            ascii_art.lonely_cat_art()
    elif character['Penelope'][0] == 5:
        if character['Penelope'][1] >= 20:
            ascii_art.happy_ending()
            ascii_art.cozy_cat_art()
        else:
            ascii_art.bad_ending()
            ascii_art.poor_kitty_art()
    else:
        print("You met Nero, Penelope, Lulu and Noah in your life, "
              "but they all end up disappearing from your life based on your decisions.")
        print("You lived the rest of your life with nothing specific happening.")
        ascii_art.bad_ending()
        ascii_art.poor_kitty_art()

    print("This is the end of a cat's story.")
    print("Thanks for playing our game.")
    print("Made By: Eunjeong(Alice) Hur, Shuyi Liu")


def get_event(event: dict, character: dict, other_character_name: str):
    """
    Adjust relationship score with other_character_name based on user's choice of script options.

    :param event: a dictionary
    :param character: a dictionary
    :param other_character_name: a string
    :precondition: other_character_name must be a string that is one of 'Nero', 'Lulu', 'Noah', 'Penelope'
    :precondition: event must be a dictionary that is retrieved from character.json file
    :precondition: character must be a dictionary
    :postcondition: If user picked gain points option, increment relationship score with
    other_character_name by gain_points score.
    :postcondition: If user picked lose points option, decrement relationship score with
    other_character_name by gain_points score.
    """
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
    """
    Replace "/mc_name" from scripts into main character name user entered.

    :param name: a string
    :param lines: a list
    :precondition: name must be main character's name that user entered
    :precondition: lines must be a list containing string
    :postcondition: replaces all '/mc_name' to name
    :return: a list containing replaced string
    """
    replaced_lines = [line.replace("/mc_name", f'\033[92m{name}\033[00m') for line in lines]

    return replaced_lines


def display_script(event: dict, character: dict) -> bool:
    """
    Display scripts that are retrieved from character.json file.

    :param event: a dictionary
    :param character: a dictionary
    :precondition: event must be a dictionary that is retrieved from character.json file
    :precondition: character must be a dictionary containing user's information
    :postcondition: displays scripts that are retrieved from character.json file
    :postcondition: gets user input which is '1' or '2' while displaying scripts
    :return: returns True if user selects gain points option. Otherwise, return False
    """
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


def check_if_goal_attained(character: dict) -> bool:
    """
    Determine whether user attained the end of events.

    :param character: a dictionary
    :precondition: character must be a dictionary containing user information
    :postcondition: checks if user reaches the critical event for any of the event characters
    :return: return True if user reaches the critical event for any of the event characters. Otherwise, return False
    """
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
    """
    Play the game.

    :postcondition: creates a 10 * 10 board by calling make_board()
    :postcondition: creates a character dictionary by calling make_character()
    :postcondition: plays a game while achieved_goal is False
    :postcondition: once achieved_gaol becomes True, ends the game and call display_ending_script()
    """
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    while not achieved_goal:
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            there_is_a_challenge = check_for_challenges(board, character)
            if there_is_a_challenge:
                achieved_goal = execute_challenge_protocol(board, character)
                if check_if_goal_attained(character):
                    achieved_goal = True
        else:
            print("You can't go that direction!")
            get_user_choice()
    display_ending_script(character)


def main():
    """
    Drive the program
    """
    game()


if __name__ == "__main__":
    main()
