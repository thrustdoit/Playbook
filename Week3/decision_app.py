#decision_app.py # This program asks the user questions and gives advice based on their answers.
# It uses conditionals (if/elif/else) and a loop to repeat until the user exits.
while True: # Loop repeats until the user chooses to stop
    # Ask the user questions
    tired = input("Are you tired? (yes/no): ").lower()
    ate = input("Did you eat today? (yes/no): ").lower()
    energy = int(input("Energy level 1-10: "))   # Decision logic using conditionals
    if tired == "no" and energy > 6:
        print("You should get some work done.")
    elif tired == "yes" and ate == "no":
        print("Eat something and rest a bit.")
    elif tired == "yes" and ate == "yes":
        print("Take a short break, then get moving.")
    else:
        print("Start with something light.")
    again = input("Run again? (yes/no): ").lower() # Ask user if they want to run the program again
    if again != "yes":
        break


        
