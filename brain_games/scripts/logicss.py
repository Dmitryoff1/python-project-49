def main():
    global name
    print("Welcome to the Brain Games!")
    name = input('May I have your name? ')
    print("Hello, " + name + "!")


def Even_or_odd():
    count = 0
    while count <= 3:
        backspace()
        inp = input("Your answer:")
        if count != 2 and answer == int(inp):
            count += 1
            print("Correct!")
        elif count == 2 and answer == int(inp):
            count += 1
            print("Correct!")
            print("Congratulation, " + name)
            break
        else:
            print(f"'{inp}' is wrong answer ;(. Correct answer was '{answer}' .")
            print(f"Let's try again, {name}!")
            break
