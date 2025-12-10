# --------------------------------------------
# loops_lists_app.py
# Purpose: Use loops and lists to store and manage items
# Author: Mohamed Kaba
# --------------------------------------------

# Create an empty list to store items
items = []

# Function to display all items in the list
def display_items():
    print("\n=== Current Items in List ===")
    if len(items) == 0:
        print("The list is empty.")
    else:
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item}")
    print("-----------------------------")


# Main menu loop (runs until user chooses to exit)
while True:

    print("\n===== MAIN MENU =====")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display all items")
    print("4. Exit program")

    choice = input("Enter your choice (1-4): ").strip()

    # Basic input validation
    if not choice.isdigit():
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    choice = int(choice)

    if choice == 1:
        # Add an item
        new_item = input("Enter the item to add: ").strip()

        if new_item == "":
            print("You cannot add an empty item.")
        else:
            items.append(new_item)
            print(f"'{new_item}' has been added.")

    elif choice == 2:
        # Remove an item
        if len(items) == 0:
            print("The list is empty. Nothing to remove.")

        else:
            display_items()
            idx = input("Enter the number of the item to remove: ").strip()

            if idx.isdigit():
                idx = int(idx)

                if 1 <= idx <= len(items):
                    removed = items.pop(idx - 1)
                    print(f"Removed '{removed}' from the list.")
                else:
                    print("That number is not in the list.")
            else:
                print("Invalid input. Please enter a valid number.")

    elif choice == 3:
        # Display items
        display_items()

    elif choice == 4:
        print("\nProgram ended. Goodbye.")
        break

    else:
        print("Please choose a valid option (1-4).")
