from random import randint


RULES_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_RANDOM_NUM = 1
MAX_RANDOM_NUM = 100


def is_prime(random_num) -> bool:

    if random_num <= 1:
        return False

    for i in range(2, int(random_num / 2) + 1):
        if random_num % i == 0:
            return False

    return True


def generate_game_data() -> tuple:
    # We generate data and ask the user a question
    random_num = randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM)
    computer_question = f'{random_num}'

    if is_prime(random_num) is True:
        target_result = 'yes'
    else:
        target_result = 'no'

    return computer_question, str(target_result)
