import random
import math


print("Welcome to the Brain Games!")


def main():
    global name
    name = input('May I have your name? ')
    print("Hello, " + name + "!")
    print("Find the greatest common divisor of given numbers.")


def random_nums1():
    random_num1 = random.randint(10, 250)
    return random_num1


def random_nums2():
    random_num2 = random.randint(5, 100)
    return random_num2


def print_expression():
    global random_num1
    global random_num2
    global summa
    random_num1 = random_nums1()
    random_num2 = random_nums2()
    print(f"Question:{random_num1} {random_num2}")
    summa = math.gcd(random_num1, random_num2)
#    print(summa)


def Even_or_odd():
    count = 0
    while count <= 3:
        print_expression()
        inp = input("Your answer:")
        if count != 2 and inp == str(summa):
            count += 1
            print("Correct!")
        elif count == 2 and inp == str(summa):
            count += 1
            print("Correct!")
            print("Congratulation, " + name)
            break
        else:
            print(f"'{inp}' is wrong answer ;(. Correct answer was '{summa}' .")
            print(f"Let's try again, {name}!")
            break


main()
random_nums1()
random_nums2()
#Even_or_odd()
