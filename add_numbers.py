"""
Simple program to add numbers
"""

def add_numbers(*args):
    """
    Add multiple numbers together
    
    Args:
        *args: Variable number of integers or floats
    
    Returns:
        The sum of all provided numbers
    """
    return sum(args)


def main():
    """Main function to demonstrate adding numbers"""
    
    # Method 1: Add two numbers
    num1 = 10
    num2 = 20
    result = num1 + num2
    print(f"Sum of {num1} and {num2} is: {result}")
    
    # Method 2: Add multiple numbers using the function
    numbers = [5, 15, 25, 35]
    result = add_numbers(*numbers)
    print(f"Sum of {numbers} is: {result}")
    
    # Method 3: User input
    print("\n--- Add numbers from user input ---")
    try:
        count = int(input("How many numbers do you want to add? "))
        numbers = []
        for i in range(count):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
        
        total = sum(numbers)
        print(f"Sum of {numbers} is: {total}")
    except ValueError:
        print("Please enter valid numbers!")


if __name__ == "__main__":
    main()
