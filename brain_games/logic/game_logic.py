from typing import NoReturn

import prompt

GREETINGS = 'Welcome to the Brain Games!'
GREETINGS_MESSAGE = 'Hello, {}!'
ASK_NAME = 'May I have your name? '
TRUE_ANSWER = 'Correct!'
FALSE_ANSWER = '''\'{}\' is wrong answer ;(. Correct answer was \'{}\'.
Let\'s try again, {}!'''
VICTORY_MESSAGE = 'Congratulations, {}!'


def run_game(game_rules: str, generate_game_data: tuple) -> NoReturn:
    # Welcome player
    print(GREETINGS)
    name = prompt.string(ASK_NAME)
    print(GREETINGS_MESSAGE.format(name))

    # We derive the rules of the game,
    # form the logic of the game and generate a cycle of rounds
    print(game_rules)


    for i in range(3):
        question, target_result = generate_game_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        # Let's find out the correct answer
        is_correct = target_result == user_answer.lower()

        # and depending on the choice of answer, call the function
        if not is_correct:
            # Executes if the last answer entered is incorrect
            print(FALSE_ANSWER.format(user_answer, target_result, name))
            return
        # Executed if the last answer entered is correct
        print(TRUE_ANSWER)
    print(VICTORY_MESSAGE.format(name))
