"""
Prototype – Service Learning Resource Tracker
Purpose: Build early version of the final project using dictionaries, tuples,
basic functions, and try/except handling.
"""

from datetime import datetime

# ------------------------------
# Data Structures
# ------------------------------

# Tuple: allowed priority options for validation
PRIORITIES = ("High", "Medium", "Low")

# List of dictionaries: each dictionary = one resource record
resources = []

next_id = 1  # auto-incrementing ID counter


# ------------------------------
# Core Prototype Functions
# ------------------------------

def add_resource(name, priority):
    """
    Adds a new resource object to the prototype.
    Uses dictionary + tuple validation.
    """
    global next_id

    if priority not in PRIORITIES:
        print("Invalid priority. Use High/Medium/Low.\n")
        return

    record = {
        "ID": next_id,
        "name": name,
        "priority": priority,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    resources.append(record)
    print(f"Added resource #{next_id}.\n")

    next_id += 1


def remove_resource(resource_id):
    """
    Removes a resource by ID.
    Demonstrates basic exception handling.
    """
    try:
        resource_id = int(resource_id)
    except ValueError:
        print("Error: ID must be a number.\n")
        return

    for item in resources:
        if item["ID"] == resource_id:
            resources.remove(item)
            print("Resource removed.\n")
            return

    print("No resource found with that ID.\n")


def display_resources():
    """
    Displays all stored prototype records.
    """
    if not resources:
        print("No resources yet.\n")
        return

    print("\n--- Prototype Resource List ---")
    for item in resources:
        print(f"ID {item['ID']}: {item['name']} (Priority: {item['priority']})")
    print()


# ------------------------------
# Simple Prototype Menu
# ------------------------------

def menu():
    """
    Small interactive menu for prototype testing.
    Uses try/except to prevent crashes.
    """
    while True:
        print("""
--- Prototype Menu ---
1. Add Resource
2. Remove Resource
3. Display Resources
4. Exit
""")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter resource name: ")
                priority = input("Enter priority (High/Medium/Low): ")
                add_resource(name, priority)

            elif choice == "2":
                rid = input("Enter ID to remove: ")
                remove_resource(rid)

            elif choice == "3":
                display_resources()

            elif choice == "4":
                print("Exiting prototype...")
                break

            else:
                print("Invalid option.\n")

        except Exception as e:
            print(f"Unexpected error: {e}\n")


# ------------------------------
# Run Prototype
# ------------------------------

menu()
