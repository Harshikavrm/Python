import random
    #Logic Building
# Program picks a random number
secret_number = random.randint(1, 100)
# The user guesses the number
print("Welcome to guessing the number game")

#The program tells them if their guess is too high, too low, or correct.
while True:
    try:
        user_Guess = int(input("Guess a number between 1 to 100:"))
        if user_Guess > secret_number:
            print("Number is too high")
        elif user_Guess < secret_number:
            print("Number is too low")
        else:
            print("Number is correct.")
            break
    except ValueError:
        print("Input the correct number.")
