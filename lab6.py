#Encoder and Decoder Program from Mason Bush and Jesse Edwards

#Encoder function
def encoder(message):
    result = ''
    for digit in message:
        new_digit = str((int(digit) + 3) % 10)
        result += new_digit
    return result


#Decoder function
def decode(user_entry):
    str_pass = ""
    storage = ""
    user_input = []
    for item in user_entry:
        if int(item):
            user_input.append(int(item) + 3)
        else:
            print("Your password contained an invalid entry.")
            break
    for item in user_input:
        str_pass += str(item - 3)
        storage += str(item)
    return str_pass


def main():
    #Loop for main program to continue
    while True:
        #Display for menu options
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        choice = input("Please enter an option: ")

        #Option Results for encoder, decoder, and quit
        if choice == "1":
            value = decode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        elif choice == "2":
            print(f"The encoded password is {encoder(value)}, and the original password is {value}.")
        elif choice == "3":
            break
        else:
            print("Invalid choice")
        print()

#Main function
if __name__ == "__main__":
    main()