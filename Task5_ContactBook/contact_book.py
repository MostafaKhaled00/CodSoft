# CodSoft
# Mostafa Khaled Mostafa
# Contact Book



"""
    Each Contact has: 1.name
                      2.number
                      3.email
                      4.address

    # Features:
                1.Add Contact
                2.View Contact List
                3.Search Contact
                4.Update Contact
                5.Delete Contact

"""

# Parallel arrays for each info set

contact_name = []
contact_number = []
contact_email = []
contact_address = []


def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")

    contact_name.append(name)
    contact_number.append(number)
    contact_email.append(email)
    contact_address.append(address)
    print("Contact Added!")


def view_list():
    count = 1
    if len(contact_name) != 0:
        for name, number in zip(contact_name,contact_number):
            print(str(count) + '.', "Name: ", name, ", Phone number: ", number)
            count += 1
    else:
        return "null"


def search():
    if len(contact_name) != 0:
        desired_contact = input("Enter the name of the contact you want to search: ")
        index = 0
        flag = False
        for name in contact_name:
            if name == desired_contact:
                print("\nContact Found!")
                print("Name: ", contact_name[index],
                      ", Phone number: ", contact_number[index],
                      ", Email: ", contact_email[index],
                      ", Address: ", contact_address[index])
                index += 1
                flag = True
            else:
                index += 1
        if not flag:
            print("Contact not found.")
    else:
        print("\nThe Contact list is empty.")


def update_contact():
    if view_list() != "null":
        index = int(input("Enter the number of the contact you want to be updated: ")) - 1
        if index in range(0,len(contact_name)):
            print("(Type 'same' if you don't want to change current info)\n")
            updated_name = input("Enter new name: ")
            updated_num = input("Enter new phone number: ")
            updated_email = input("Enter new email: ")
            updated_address = input("Enter new address: ")

            if updated_name != "same":
                contact_name[index] = updated_name

            if updated_num != "same":
                contact_number[index] = updated_num

            if updated_email != "same":
                contact_email[index] = updated_email

            if updated_address != "same":
                contact_address[index] = updated_address

            print("\nContact updated!")
        else:
            print("Invalid number!")

    else:
        print("\nContact list is empty.")


def del_contact():
    if view_list() != "null":
        # view_list()
        index = int(input("\nEnter the number of the contact you want to delete: ")) - 1
        if index in range(0,len(contact_name)):
            contact_name.pop(index)
            contact_number.pop(index)
            contact_email.pop(index)
            contact_address.pop(index)
            print("Contact deleted!")

        else:
            print("Invalid number!")
    else:
        print("\nContact list is empty.")


while True:
    print("\n*********************")
    print("    Contact Book")
    print("*********************")
    print("\n1. Add Contact"
          "\n2. View Contact List"
          "\n3. Search Contact"
          "\n4. Update Contact"
          "\n5. Delete Contact"
          "\n6. Exit")

    decision = int(input("\nType the number of the feature you want: "))
    if decision == 1:
        add_contact()

    elif decision == 2:
        if view_list() == "null":
            print("\nContact list is empty.")

    elif decision == 3:
        search()

    elif decision == 4:
        update_contact()

    elif decision == 5:
        del_contact()

    elif decision == 6:
        print("Thank you for using my application!")
        exit()


