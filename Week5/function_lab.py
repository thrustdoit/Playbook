# --------------------------------------------------------
# function_lab.py
# Purpose: Practice creating reusable Python functions
# Author: Mohamed Kaba
# --------------------------------------------------------


# Function 1
# Purpose: Calculate the area of a rectangle
# Inputs: width (float), height (float)
# Output: area (float)
def rectangle_area(width, height):
    return width * height


# Function 2
# Purpose: Determine whether a number is even or odd
# Input: number (int)
# Output: "even" or "odd" (string)
def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


# Function 3
# Purpose: Combine a first name and last name into a full name
# Inputs: first (string), last (string)
# Output: full name (string)
def full_name(first, last):
    return first + " " + last


# --------------------------------------------------------
# Main Program
# --------------------------------------------------------
def main():

    print("=== Function Lab Output ===")

    # Test Function 1
    area = rectangle_area(5, 3)
    print("Area of rectangle (5 x 3):", area)

    # Test Function 2
    result = even_or_odd(12)
    print("12 is:", result)

    # Test Function 3
    name = full_name("Mohamed", "Kaba")
    print("Full name:", name)


# Call the main function
main()
