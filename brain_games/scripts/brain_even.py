import random


print("Welcome to the Brain Games!")


def main():
    global name
    name = input('May I have your name? ')
    print("Hello, " + name + "!")
    print("Answer ""yes"" if the number is even, otherwise answer ""no"".")


random_num = 0


def print_num():
    global random_num
    random_num = random.randint(1, 100)
    print("Question:" + str(random_num))
    return random_num


def Even_or_odd():
    if random_num % 2 == 0:
        return "yes"
    else:
        return "no"


def game_counter():
    counter = 0
    while counter <= 3:
        print_num()
        if counter != 2 and input("Your answer:") == Even_or_odd():
            counter += 1
            print("Correct!")
        elif counter == 2 and input("Your answer:") == Even_or_odd():
            counter += 1
            print("Correct!")
            print("Congratulation, " + name)
            break
        else:
            counter = 0
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + "!")
            break


main()
