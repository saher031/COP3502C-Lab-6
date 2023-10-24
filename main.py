# Saher Alwani
def menu():  # Print menu options
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


def encoder(user_password):  # Encoder function
    encoded_pass = ""
    for i in user_password:
        if int(i) < 7:  # If num is less than 7, add 3
            num = int(i) + 3
        else:
            num = int(i) + 3  # If num is greater than or equal to seven, add 3 but only keep the last digit
            num = str(num)[1]
        encoded_pass += str(num)
    return encoded_pass  # Output string of encoded numbers

if __name__ == '__main__':
    while True:  # main loop
        print()
        menu()
        option = int(input("Please enter an option: "))  # Ask user to select option

        if option == 1:  # User will enter password to encode
            user_password = input("Please enter your password to encode: ")
            encoded_pass = encoder(user_password)
            print("Your password has been encoded and stored!")
            print(encoded_pass)

        if option == 2:
            pass

        if option == 3:  # Exit the loop
            break
