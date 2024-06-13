import random


print("Welcome to the Brain Games!")


def main():
    global name
    name = input('May I have your name? ')
    print("Hello, " + name + "!")
    print("What is the result of the expression?")


def random_nums1():

    random_num1 = random.randint(1, 20)
    return random_num1


def random_nums2():

    random_num2 = random.randint(1, 20)
    return random_num2


def random_math_operation():

    math_operations = ["+", "-", "*"]
    math_operation = random.choice(math_operations)
    return math_operation


def print_expression():
    global random_num1
    global random_num2
    global math_operation
    random_num1 = random_nums1()
    math_operation = random_math_operation()
    random_num2 = random_nums2()
    print(f"Question:{random_num1} {math_operation} {random_num2}")
    sum_num()


def sum_num():
    global summa
    if math_operation == "+":
        summa = random_num1 + random_num2
    elif math_operation == "-":
        summa = random_num1 - random_num2
    else:
        summa = random_num1 * random_num2
#    print(summa)
    return summa


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
random_math_operation()
#Even_or_odd()
