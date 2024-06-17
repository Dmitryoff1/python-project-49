from random import randint, choice
from typing import Callable

from brain_games.logic.game_logic import run_game

RULES_MESSAGE = 'What is the result of the expression?'

MIN_RANDOM_NUM = 1
MAX_RANDOM_NUM = 100

OPERATOR_PLUS = '+'
OPERATOR_MINUS = '-'
OPERATOR_MULTIPLY = '*'

ARITHMETIC_OPERATIONS = (OPERATOR_MINUS, OPERATOR_PLUS, OPERATOR_MULTIPLY)


def generate_game_data() -> tuple:
    # We generate data and ask the user a question
    random_number1 = randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM)
    random_number2 = randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM)
    operation = choice(ARITHMETIC_OPERATIONS)
    question = f'{random_number1} {operation} {random_number2}'

    # Determining the correct answer
    target_result = False  # Default value
    if operation == OPERATOR_PLUS:
        target_result = random_number1 + random_number2
    elif operation == OPERATOR_MINUS:
        target_result = random_number1 - random_number2
    elif operation == OPERATOR_MULTIPLY:
        target_result = random_number1 * random_number2

    return question, target_result


def calc_game() -> Callable:
    run_game(RULES_MESSAGE, generate_game_data)
