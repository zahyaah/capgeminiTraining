import random 

def generateRandomNumber():
    '''
        Generate a random number between 1 and 100.
    '''
    originalNumber = random.randrange(1, 101)
    return originalNumber

def compareGuess(userGuess, originalNumber, attempts):
    '''
        Compare the user's guess with the original number and provide feedback.
    '''
    if (userGuess > originalNumber):
        print("Too high. Try again ;)")
    elif (userGuess < originalNumber):
        print("Too low. Try again.")
    else:
        print(f"Congratulations. You found the correct number {userGuess} in {attempts} attempts")

def main():
    originalNumber = generateRandomNumber()
    attempts = 0

    while True:
        guess = input("Select a number between 1 and 100: ")
        if not guess.isdigit():
            print("Invalid input!")
        else:
            guessNumber = int(guess)
            if guessNumber < 1 or guessNumber > 100:
                print("Invalid input! Please select a number between 1 and 100.")
            else:
                attempts += 1
                compareGuess(guessNumber, originalNumber, attempts)

                if (guessNumber == originalNumber):
                    break; 
main()