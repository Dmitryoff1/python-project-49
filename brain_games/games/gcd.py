import math
from random import randint


RULES_MESSAGE = 'Find the greatest common divisor of given numbers.'
MIN_RANDOM_NUM = 1
MAX_RANDOM_NUM = 100


def generate_game_data() -> tuple:
    # We generate data and ask the user a question
    random_num1 = randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM)
    random_num2 = randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM)
    computer_question = f'{random_num1} {random_num2}'

    # Determining the correct answer
    target_result = math.gcd(random_num1, random_num2)
    return computer_question, str(target_result)
