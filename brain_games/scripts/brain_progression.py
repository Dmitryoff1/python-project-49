import random


print("Welcome to the Brain Games!")


def main():
    global name
    name = input('May I have your name? ')
    print("Hello, " + name + "!")
    print("Find the greatest common divisor of given numbers.")

def random_nums1():
    global random_num1
    random_num1 = random.randint(1, 20)
    return random_num1


def random_nums2():
    global random_num2
    random_num2 = random.randint(1, 10)
    return random_num2


def randoms_index():
    global random_index
    random_index = random.randint(1, 9)
    return random_index


def arithmetic_progression():
    global lists
    lists = list(range(random_num1, 100, random_num2))
    return lists

def len_progression():
    if len(arithmetic_progression()) >= 10:
        return (lists[0:10])
    elif len(arithmetic_progression()) < 10 and len(arithmetic_progression()) >= 5:
        return (lists)
    else:
        pass

def backspace():
    global symbol
    spisk = len_progression()
    numb = randoms_index()
    symbol = spisk[numb]
    spisk[numb] = ".."
    print(' '.join(str(el) for el in spisk))
    print(symbol)




def Even_or_odd():
    count = 0
    while count <= 3:
        backspace()
        inp = input("Your answer:")
        if count != 2 and symbol == int(inp):
            count += 1
            print("Correct!")
        elif count == 2 and symbol == int(inp):
            count += 1
            print("Correct!")
            print("Congratulation, " + name)
            break
        else:
            print(f"'{inp}' is wrong answer ;(. Correct answer was '{symbol}' .")
            print(f"Let's try again, {name}!")
            break
main()
random_nums1()
random_nums2()

Even_or_odd()