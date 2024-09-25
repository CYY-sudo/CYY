import random
import sys
import os

def shutdown():
    if sys.platform.startswith('win'):
        os.system('shutdown /s /t 1')
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system('sudo shutdown -h now')
    else:
        print("Unknown operating system, unable to execute shutdown command")

def guess_number():
    try:
        number = random.randint(1, 100)
        print("I'm thinking of a number between 1 and 100. You have only one chance to guess it!")

        try:
            guess = int(input("Enter your guess: "))

            if guess == number:
                print(f"Congratulations! You guessed it correctly.")
            else:
                print(f"Sorry, the correct number was {number}.")
                print("WOMPWOMP")
                shutdown()
        except ValueError:
            print("Please enter a valid number!")
            print("WOMPWOMP")
            shutdown()
    except Exception as e:
        print(f"Game error occurred: {e}")
        print("WOMPWOMP")
        shutdown()

if __name__ == "__main__":
    guess_number()