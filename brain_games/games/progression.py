from random import randint


RULES_MESSAGE = 'What number is missing in the progression?'

# Data for progression
START_VALUE_MIN = 1
START_VALUE_MAX = 50

STEP_VALUE_MIN = 3
STEP_VALUE_MAX = 30

LENGTH_VALUE_MIN = 5
LENGTH_VALUE_MAX = 10


def generate_game_data() -> tuple:
    # We generate data and ask the user a question
    start_value = randint(
        START_VALUE_MIN, START_VALUE_MAX
    )
    length_value = randint(
        LENGTH_VALUE_MIN, LENGTH_VALUE_MAX
    )

    # So that the sequence can be descending,
    # raise to the power (-1) from 1 to 2 times in step_value_sign
    # This will save us from the possibility of a zero step with randint(-n, n)
    step_value_sign = (-1) ** randint(1, 2)
    step_value = step_value_sign * randint(
        STEP_VALUE_MIN, STEP_VALUE_MAX
    )

    progression = []
    progression_max_value = start_value + (length_value * step_value)
    for i in range(start_value, progression_max_value, step_value):
        progression.append(str(i))

    # Determine the number and replace it with two dots
    index_skip_value = randint(0, length_value - 1)
    target_result = progression[index_skip_value]
    progression[index_skip_value] = '..'
    question = " ".join(progression)
    return question, str(target_result)
