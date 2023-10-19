# CodSoft Python internship
# Mostafa Khaled Mostafa
# Password Generator task

import random
import string


def password_gen(length):
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(characters) for i in range(length))
    return password


while True:
    print("\n**********************************")
    print("  Password Generator application")
    print("**********************************")

    while True:
        length = int(input("\nType your desired password length: "))
        if length < 8:
            print("Minimum number of characters is 8.")
            continue
        else:
            break
    password = password_gen(length)
    print("Your password is: ", password)

    if (input("Would you like to generate another one? (yes/no) ").lower() == 'yes'):
        continue
    else:
        print("Thank you for using my application!")
        break
