import random
import sys

random_number = random.randint(1, 10)
tries = 0
tries_remaining = 5
has_won = False


def test_number(guess_num, tries, tries_remaining, has_won):
    if not guess_num > 0 or not guess_num < 11:
        print("That number is not between 1 and 10.")
        tries -= 1
        tries_remaining += 1

    elif guess_num == random_number:
        print("Congratulations! You are correct!")
        print("It took you {} tries.".format(tries))
        has_won = True

    elif guess_num < random_number:
        if tries_remaining > 0:
            print("I'm sorry, that number is low. You have {} tries remaining.".format(int(tries_remaining)))
        else:
            print("Sorry, but my number was {}".format(random_number))
            print("You are out of tries. Better luck next time.")

    elif guess_num > random_number:
        if tries_remaining > 0:
            print("I'm sorry, that number is high. You have {} tries remaining.".format(int(tries_remaining)))
        else:
            print("Sorry, but my number was {}".format(random_number))
            print("You are out of tries. Better luck next time.")
            sys.exit()

    return (tries, tries_remaining, has_won)


def main(random_number, tries, tries_remaining, has_won):
    while tries < 5:
        guess = input("Guess a random number between 1 and 10. ")
        tries += 1
        tries_remaining -= 1

        try:
            guess_num = int(guess)
            tries, tries_remaining, has_won = test_number(guess_num, tries, tries_remaining, has_won)

        except:
            print("That's not a whole number!")
            tries -= 1
            tries_remaining += 1

        if has_won:
            break

main(random_number, tries, tries_remaining, has_won)
        