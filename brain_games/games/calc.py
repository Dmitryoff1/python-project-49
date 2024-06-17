from random import randint, choice


RULES_MESSAGE = 'What is the result of the expression?'

MIN_RANDOM_NUM = 1
MAX_RANDOM_NUM = 100

OPERATOR_PLUS = '+'
OPERATOR_MINUS = '-'
OPERATOR_MULTIPLY = '*'

ARITHMETIC_OPERATIONS = (OPERATOR_MINUS, OPERATOR_PLUS, OPERATOR_MULTIPLY)


def generate_game_data() -> tuple:
    # We generate data and ask the user a question
    random_num1 = randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM)
    random_num2 = randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM)
    operation = choice(ARITHMETIC_OPERATIONS)
    question = f'{random_num1} {operation} {random_num2}'
    # Determining the correct answer
    target_result = False  # Default value
    if operation == OPERATOR_PLUS:
        target_result = random_num1 + random_num2
    elif operation == OPERATOR_MINUS:
        target_result = random_num1 - random_num2
    elif operation == OPERATOR_MULTIPLY:
        target_result = random_num1 * random_num2
    return question, str(target_result)
