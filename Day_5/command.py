def arithmetic_operations():
    print("\n--- Arithmetic Operations ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
 
    choice = input("Choose an operation (1/2/3/4): ")
 
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        return
 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
 
    if choice == '1':
        print(f"The result of addition is: {num1 + num2}")
    elif choice == '2':
        print(f"The result of subtraction is: {num1 - num2}")
    elif choice == '3':
        print(f"The result of multiplication is: {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"The result of division is: {num1 / num2}")
        else:
            print("Error: Division by zero")
 
def string_manipulations():
    print("\n--- String Manipulations ---")
    print("1. Reverse String")
    print("2. Convert to Uppercase")
    print("3. Count Vowels")
 
    choice = input("Choose an operation (1/2/3): ")
 
    if choice not in ['1', '2', '3']:
        print("Invalid choice")
        return
 
    user_string = input("Enter a string: ")
 
    if choice == '1':
        print(f"The reversed string is: {user_string[::-1]}")
    elif choice == '2':
        print(f"The string in uppercase is: {user_string.upper()}")
    elif choice == '3':
        vowels = 'aeiouAEIOU'
        count = sum(1 for char in user_string if char in vowels)
        print(f"The number of vowels in the string is: {count}")
 
def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Perform Arithmetic Operations")
        print("2. Perform String Manipulations")
        print("3. Exit")
 
        choice = input("Enter your choice (1/2/3): ")
 
        if choice == '1':
            arithmetic_operations()
        elif choice == '2':
            string_manipulations()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
 
if __name__ == "__main__":
    main()
