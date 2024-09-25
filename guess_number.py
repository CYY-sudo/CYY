import random
import sys
import os
import atexit

def shutdown():
    if sys.platform.startswith('win'):
        os.system('shutdown /s /t 1')
    elif sys.platform.startswith('linux'):
        os.system('sudo shutdown -h now')
    elif sys.platform.startswith('darwin'):
        os.system('sudo shutdown -h now')
    else:
        print("Unknown operating system")

atexit.register(shutdown)

def guess_number():
    try:
        number = random.randint(1, 100)
        print("Guess a number between 1-100. You have only one chance!")

        try:
            guess = int(input("Enter your guess: "))

            if guess == number:
                print("You got it right!")
            else:
                print(f"Sorry, the correct number was {number}. Womp Womp")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"Game error occurred: {e}")
    finally:
        atexit.unregister(shutdown)

if __name__ == "__main__":
    guess_number()