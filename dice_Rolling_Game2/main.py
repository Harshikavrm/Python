import random

#def dice_rolling_game():
 #   dice1 = random.randint(1, 6)
  #  dice2 = random.randint(1, 6)
   # return dice1, dice2

#print("welcome to the dice rolling game.")

#while True:
 #   choice = input("Do you want to play roll the Dice? (yes/no): ").strip().lower()
#
 #      dice1, dice2 = dice_rolling_game()
  #      print(f"({dice1} , {dice2})")
   # elif choice == "no":
    #    print("Thank you for playing!")
     #   break
    #else:
     #   print("Invalid choice. Please type 'yes' or 'no'.")


def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, 6))
    return results

print("welcome to the dice rolling game.")

roll_count = 0

while True:
    choice = input("Do you want to play roll the Dice? (yes/no): ").strip().lower()
    if choice == "yes":
        try:
            num_dice = int(input("How many dice do you want to roll? "))
            if num_dice < 1:
                print("You must roll at least one die.")
                continue

            results = roll_dice(num_dice)
            roll_count += 1
            print(f"({', '.join(str(r) for r in results)})")
            print(f"Total rolls so far: {roll_count}")

        except  ValueError:
            print("Please enter a valid number.")
    elif choice == "no":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")


