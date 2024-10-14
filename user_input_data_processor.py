#task1
def user_input():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    while True:
        

        valid_first = len(first_name) >= 2
        valid_last = len(last_name) >= 2


        if not valid_first:
            print("Error: First name must be at least 2 characters long.")
            first_name = input("Re-enter your first name: ")

        elif not valid_last:
            print("Error: Last name must be at least 2 characters long.")
            last_name = input("Re-enter your last name: ")
        else:
            valid_first and valid_last
            print("Names are valid.")
            break

        
user_input()