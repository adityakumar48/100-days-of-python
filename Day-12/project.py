from random import randint


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


answer = randint(1, 100)

guss = int(input("Make a guess: "))


def guess_number():
    chosen_number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {chosen_number}")
    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}.")
    elif guess > chosen_number:
        print("Too high.")
        return guess_number()
    elif guess < chosen_number:
        print("Too low.")
        return guess_number()


guess_number()
