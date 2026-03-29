# Day 5 - To Do List App

tasks = []

print("Welcome to your To-Do List!")
print("------------------------------")

while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(str(i) + ". " + task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove!")
        else:
            for i, task in enumerate(tasks, 1):
                print(str(i) + ". " + task)
            num = int(input("Enter task number to remove: "))
            removed = tasks.pop(num - 1)
            print("Removed: " + removed)

    elif choice == "4":
        print("Goodbye Sparkle! Keep crushing it! 💪")
        break

    else:
        print("Invalid choice! Please enter 1-4")
