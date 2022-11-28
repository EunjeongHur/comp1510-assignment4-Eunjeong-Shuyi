"""
Member #1 Student Name: Alice Hur
Member #1 Student Number: A01272954

Member #2 Student Name: Shuyi Liu
Member #2 Student Number: A01178380
"""


def make_board(rows, columns):
    pass


def make_character():
    pass


def describe_current_location(board, character):
    pass


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
    game()


if __name__ == "__main__":
    main()
