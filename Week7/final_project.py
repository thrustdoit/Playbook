# --------------------------------------------------------------
# service_learning_final.py
# Final Integrated Service-Learning Prototype (Weeks 1–7)
# Author: Mohamed Kaba
#
# Features:
# - User input and menu system
# - Arithmetic and logical operations
# - Conditional statements (if/elif/else)
# - Loops and iteration
# - Modular functions with parameters and returns
# - Dictionaries and tuples for structured data
# - File I/O (save/load JSON)
# - Exception handling
# - Fully debugged and formatted
# --------------------------------------------------------------

import json

DATA_FILE = "resources.json"


# --------------------------------------------------------------
# Load existing data from file
# --------------------------------------------------------------
def load_resources():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}   # No file yet
    except json.JSONDecodeError:
        print("Warning: Data file unreadable. Starting fresh.")
        return {}


# --------------------------------------------------------------
# Save data to file
# --------------------------------------------------------------
def save_resources(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error saving data:", e)


# Load resources at program start
resources = load_resources()


# --------------------------------------------------------------
# Core Functions
# --------------------------------------------------------------
def add_resource(resource_id, description, priority):
    """
    Adds a resource to the main dictionary.
    """
    resources[resource_id] = (description, priority)
    save_resources(resources)


def remove_resource(resource_id):
    """
    Removes a resource if it exists.
    Returns True if successful, False otherwise.
    """
    try:
        del resources[resource_id]
        save_resources(resources)
        return True
    except KeyError:
        return False


def display_resources():
    """
    Prints all stored resources in a clean format.
    """
    print("\n=== Community Resource List ===")

    if not resources:
        print("No resources found.")
    else:
        for rid, details in resources.items():
            print(f"ID {rid}: {details[0]} (Priority: {details[1]})")

    print("--------------------------------")


def search_resource(keyword):
    """
    Searches resources by keyword.
    Returns a list of matches.
    """
    results = []

    for rid, details in resources.items():
        if keyword.lower() in details[0].lower():
            results.append((rid, details))

    return results


# --------------------------------------------------------------
# Menu Loop
# --------------------------------------------------------------
def menu():

    while True:

        print("\n=== Service-Learning Resource Manager ===")
        print("1. Add Resource")
        print("2. Remove Resource")
        print("3. View All Resources")
        print("4. Search Resources")
        print("5. Exit Program")

        choice = input("Enter choice (1-5): ").strip()

        # Validate numeric input
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice)

        # ----------------------------
        # Option 1: Add Resource
        # ----------------------------
        if choice == 1:
            try:
                rid = int(input("Enter new resource ID: "))
                desc = input("Enter description: ")
                priority = input("Enter priority (High/Medium/Low): ")

                add_resource(rid, desc, priority)
                print("Resource added successfully.")

            except ValueError:
                print("Invalid ID. Please enter a numeric ID.")

        # ----------------------------
        # Option 2: Remove Resource
        # ----------------------------
        elif choice == 2:
            try:
                rid = int(input("Enter resource ID to remove: "))

                if remove_resource(rid):
                    print("Resource removed successfully.")
                else:
                    print("Resource ID not found.")

            except ValueError:
                print("Invalid ID.")

        # ----------------------------
        # Option 3: Display Resources
        # ----------------------------
        elif choice == 3:
            display_resources()

        # ----------------------------
        # Option 4: Search Resources
        # ----------------------------
        elif choice == 4:
            keyword = input("Enter keyword to search: ")
            matches = search_resource(keyword)

            if matches:
                print("\nSearch Results:")
                for rid, details in matches:
                    print(f"ID {rid}: {details[0]} (Priority: {details[1]})")
            else:
                print("No matching resources found.")

        # ----------------------------
        # Option 5: Exit
        # ----------------------------
        elif choice == 5:
            print("\nExiting program... Goodbye.")
            break

        # ----------------------------
        # Invalid Option
        # ----------------------------
        else:
            print("Please choose a valid option (1–5).")


# --------------------------------------------------------------
# Main Program
# --------------------------------------------------------------
def main():
    print("\n=== Final Integrated Service-Learning Prototype ===")
    menu()


# Run the program
main()
