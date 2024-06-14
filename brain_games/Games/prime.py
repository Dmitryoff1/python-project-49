from random import randint
from typing import Callable

from brain_games.logic.game_logic import run_game

RULES_MASSAGE  = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_RANDOM_NUM = 1
MAX_RANDOM_NUM = 100


def is_prime(random_number) -> bool:

    if random_number <= 1:
        return False

    for i in range(2, int(random_number / 2) + 1):
        if random_number % i == 0:
            return False

    return True


def generate_game_data() -> tuple:
    # Генерируем данные и задаем вопрос пользователю
    random_number = randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM)
    computer_question = f'{random_number}'

    if is_prime(random_number) == True:
        target_result = 'yes'
    else:
        target_result = 'no'

    return computer_question, target_result


def prime_game() -> Callable:
    run_game(RULES_MASSAGE , generate_game_data)
