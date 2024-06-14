import math
from random import randint
from typing import Callable

from brain_games.logic.game_logic import run_game

RULES_MASSAGE = 'Find the greatest common divisor of given numbers.'

MIN_RANDOM_NUM = 1
MAX_RANDOM_NUM = 100


def generate_game_data() -> tuple:
    # Генерируем данные и задаем вопрос пользователю
    random_number1 = randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM)
    random_number2 = randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM)
    computer_question = f'{random_number1} {random_number2}'

    # Определяем правильный ответ
    target_result = math.gcd(random_number1, random_number2)

    return computer_question, target_result


def gcd_game() -> Callable:
    run_game(RULES_MASSAGE, generate_game_data)
