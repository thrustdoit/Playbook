# final_project.py
# Service-Learning Project – Final Version
# Author: Mohamed Kaba
# Purpose: Event Sign-In Tracker using lists, dictionaries, tuples, loops, and exception handling.


# -----------------------------------------------------------
# DATA STRUCTURES
# -----------------------------------------------------------

# Tuple: event details
event_info = ("Community Workshop", "Hocking College", "12/15/2025")

# List: holds dictionaries for each student
attendance_list = []


# -----------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------

def display_event_details():
    """Show event tuple details."""
    print("\n--- Event Information ---")
    print(f"Event Name : {event_info[0]}")
    print(f"Location   : {event_info[1]}")
    print(f"Date       : {event_info[2]}")
    print("--------------------------\n")


def add_student():
    """Add a student to the attendance list with error handling."""
    try:
        name = input("Enter student name: ").strip()
        if name == "":
            raise ValueError("Name cannot be empty.")

        major = input("Enter major: ").strip()
        year = input("Enter class year (e.g., Freshman, Sophomore): ").strip()

        # Dictionary for each student
        student_record = {
            "name": name,
            "major": major,
            "year": year
        }

        attendance_list.append(student_record)

        print(f"\n✔ {name} has been added.\n")

    except ValueError as e:
        print(f"Error: {e}\n")


def remove_student():
    """Remove a student by name with validation."""
    try:
        target = input("Enter the name to remove: ").strip()
        removed = False

        for student in attendance_list:
            if student["name"].lower() == target.lower():
                attendance_list.remove(student)
                removed = True
                print(f"\n✔ {target} has been removed.\n")
                break

        if not removed:
            raise LookupError("Student not found.")

    except LookupError as e:
        print(f"Error: {e}\n")


def display_all():
    """Display all students currently signed in."""
    print("\n--- Attendance List ---")

    if len(attendance_list) == 0:
        print("No students signed in yet.")
    else:
        for i, student in enumerate(attendance_list, start=1):
            print(f"{i}. {student['name']} | {student['major']} | {student['year']}")

    print("-------------------------\n")


def save_report():
    """Save attendance to a text file."""
    try:
        filename = "attendance_report.txt"

        with open(filename, "w") as file:
            file.write("=== Attendance Report ===\n")
            file.write(f"Event: {event_info[0]} at {event_info[1]} on {event_info[2]}\n\n")

            if len(attendance_list) == 0:
                file.write("No attendees recorded.\n")
            else:
                for student in attendance_list:
                    line = f"{student['name']} - {student['major']} - {student['year']}\n"
                    file.write(line)

        print(f"\n✔ Report saved as {filename}\n")

    except Exception as e:
        print(f"Unexpected error while saving: {e}\n")


# -----------------------------------------------------------
# MAIN MENU LOOP
# -----------------------------------------------------------

def main():
    print("===================================")
    print("   EVENT SIGN-IN TRACKING SYSTEM   ")
    print("===================================\n")

    while True:
        try:
            print("Choose an option:")
            print("1. View Event Info")
            print("2. Add Student")
            print("3. Remove Student")
            print("4. View Attendance List")
            print("5. Save Report")
            print("6. Exit\n")

            choice = int(input("Enter choice (1-6): "))

            if choice == 1:
                display_event_details()

            elif choice == 2:
                add_student()

            elif choice == 3:
                remove_student()

            elif choice == 4:
                display_all()

            elif choice == 5:
                save_report()

            elif choice == 6:
                print("\nExiting program... Goodbye!\n")
                break

            else:
                print("\nChoose a valid option (1-6).\n")

        except ValueError:
            print("\nInvalid input — numbers only please.\n")

        except Exception as e:
            print(f"\nUnexpected error: {e}\n")


# -----------------------------------------------------------
# RUN PROGRAM
# -----------------------------------------------------------

if __name__ == "__main__":
    main()
