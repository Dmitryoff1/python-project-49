from random import randint
from typing import Callable

from brain_games.logic.game_logic import run_game

RULES_MASSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_RANDOM_NUM = 1
MAX_RANDOM_NUM = 100


def is_even(random_number: int) -> tuple:

    if random_number % 2 == 0:
        return True
    else:
        return False


def generate_game_data() -> tuple:
    # Генерируем данные и задаем вопрос пользователю
    random_number = randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM)
    computer_question = f'{random_number}'

    # Определяем правильный ответ
    if is_even(random_number) == True:
        target_result = 'yes'
    else:
        target_result = 'no'

    return computer_question, target_result


def even_game() -> Callable:
    run_game(RULES_MASSAGE, generate_game_data)
