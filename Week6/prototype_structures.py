# ----------------------------------------------------------
# prototype_structures.py
# Purpose: Service-Learning Prototype using dictionaries,
#          tuples, and exception handling.
# Author: Mohamed Kaba
# ----------------------------------------------------------

# Sample structured data (tuples inside a dictionary)
# Each entry represents a community resource or task:
# (description, priority level)
resources = {
    1: ("Food distribution site", "High"),
    2: ("After-school tutoring", "Medium"),
    3: ("Community clean-up event", "Low")
}


# Function: Add a new resource using a tuple
def add_resource(resource_id, description, priority):
    resources[resource_id] = (description, priority)
    return resources


# Function: Remove a resource by ID
def remove_resource(resource_id):
    try:
        del resources[resource_id]
        return True
    except KeyError:
        return False


# Function: Display all resources
def display_resources():
    print("\n=== Current Community Resources ===")
    for key, value in resources.items():
        print(f"ID {key}: {value[0]}  (Priority: {value[1]})")
    print("------------------------------------")


# Main program demonstrating prototype workflow
def main():

    print("\n=== Service-Learning Prototype (Tuples & Dictionaries) ===")

    # Show starting data
    display_resources()

    # Attempt to add a new resource
    print("\nAdding new resource...")
    add_resource(4, "Clothing donation drop-off", "High")

    # Display updated resources
    display_resources()

    # Try/Except example for removing an ID
    print("\nTrying to remove resource with ID 10...")
    try:
        success = remove_resource(10)
        if not success:
            raise KeyError("Resource ID does not exist.")
    except KeyError as e:
        print("Error:", e)

    # Correct removal
    print("\nRemoving resource with ID 2...")
    remove_resource(2)

    # Final display
    display_resources()

    print("\nPrototype completed successfully without errors.")


# Run the program
main()
