# CodSoft
# Mostafa Khaled Mostafa
# To-Do List application


# functions:
#   1.add tasks
#   2.remove task
#   3.update
#   4.cross off


def show_list():
    print("\n***************************")
    print("Your To-Do list: ")
    count = 1
    count2 = 1
    for i in tasks:
        print(str(count)+'.', i)
        count += 1
    print("\nCompleted Tasks: ")
    for i in tasks_done:
        print(str(count2)+'.', i)
        count2 += 1


def add_task():
    added = input("Type your task: ")
    tasks.append(added)
    # while True:
    #     again = input("Would you like to add another task? (y/n) \n").lower()
    #     if again == 'y':
    #         added = input("Type your task: ")
    #         tasks.append(added)
    #     else:
    #         break


def remove_task():
    to_be_rem = int(input("Select the number of the task to be removed: ")) - 1
    if to_be_rem in range(0, len(tasks)):
        tasks.pop(to_be_rem)
        # while True:
        #     if (input("Would you like to remove another task? (y/n) ").lower() == 'y'):
        #         to_be_rem = int(input("Select the number of the task to be removed: "))
        #         tasks.pop(to_be_rem - 1)
        #     else:
        #         break
    else:
        print("Invalid task number!")


def update_task():
    updated_num = int(input("\nSelect the number of the To-Do to be updated: ")) - 1
    if updated_num in range(0, len(tasks)):
        updated_task = input("Type your task: ")
        tasks[updated_num] = updated_task
        # while True:
        #     if (input("Would you like to update another task? (y/n) ").lower() == 'y'):
        #         updated_num = int(input("\nSelect the number of the To-Do to be updated: "))
        #         updated_task = input("Type your task: ")
        #         tasks[updated_num - 1] = updated_task
        #     else:
        #         break
    else:
        print("Invalid task number!")


def done():
    completed_num = int(input("\nSelect the number of the task to be crossed off: ")) - 1
    if completed_num in range(0, len(tasks)):
        tasks_done.append(tasks[completed_num])
        tasks.pop(completed_num)
    else:
        print("Invalid task number!")


# def del_all():
#     last_chance = input("Are you sure you to delete all the tasks? (y/n) \n")
#     if last_chance.lower() == "y":
#         tasks.clear()
#     print("All tasks have been deleted")


def exit_prog():
    print("Thank you for using my application!")
    exit()


tasks = []
tasks_done = []

while True:
    print("\n***************************")
    print("  To-Do List application   ")
    print("***************************\n")
    print("1. Show All Tasks")
    print("2. Add Task")
    print("3. Cross Off Task")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Exit")
    print("\n***************************")
    print("What do you want to do? ")
    decision = int(input("Type feature number: "))
    if decision == 1:
        if len(tasks) == 0 and len(tasks_done) == 0:
            print("\nNo task yet!\n")
        else:
            show_list()
    elif decision == 2:
        add_task()
    elif decision == 3:
        if len(tasks) == 0:
            print("\nInvalid No task yet!\n")
        else:
            show_list()
            done()
    elif decision == 4:
        if len(tasks) == 0:
            print("\nInvalid No task yet!\n")
        else:
            show_list()
            update_task()
    elif decision == 5:
        if len(tasks) == 0:
            print("\nInvalid No task yet!\n")
        else:
            show_list()
            remove_task()
    elif decision == 6:
        exit_prog()
    else:
        print()
        print("Invalid choice")
        continue
