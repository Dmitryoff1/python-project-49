import random


def main():
    global name
    print("Welcome to the Brain Games!")
    name = input('May I have your name? ')
    print("Hello, " + name + "!")


print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")


def random_nums():

    randoms = random.randint(1, 20)
    return randoms


def prime_nums():
    global answ
    list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    answ = ""
    randoms = random_nums()
    result = randoms in list
    print(randoms)
    if result is True:
        answ = "yes"
        return "yes"
    else:
        answ = "no"
        return "no"


def Even_or_odd():
    count = 0
    while count <= 3:
        prime_nums()
        inp = input("Your answer:")

        if count != 2 and answ == inp:
            count += 1
            print("Correct!")
        elif count == 2 and answ == inp:
            count += 1
            print("Correct!")
            print("Congratulation, " + name)
            break
        else:
            print(f"'{inp}' is wrong answer ;(. Correct answer was '{answ}' .")
            print(f"Let's try again, {name}!")
            break


main()
