print("=== Welcome to the GKS Student Task Manager ===")

# 1. Create an empty List data structure to store your tasks
todo_list = []

# 2. Main interactive menu loop
while True:
    print("\n--- MENU ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Completed Task")
    print("4. Quit Program")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    # Logic matrix to handle user choices
    if choice == "1":
        print("\n📝 CURRENT TASKS:")
        if not todo_list:
            print("Your list is completely empty! Great job.")
        else:
            # Loop through the list and print tasks with an index number
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
                
    elif choice == "2":
        new_task = input("Enter the task description: ").strip()
        if new_task:
            todo_list.append(new_task)  # Adds the item into the list array
            print(f"✅ Added successfully: '{new_task}'")
        else:
            print("❌ Task description cannot be blank.")
            
    elif choice == "3":
        if not todo_list:
            print("❌ Nothing to remove. Your list is already empty.")
        else:
            print("\n📝 Select the task number you finished:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
            
            try:
                task_num = int(input("\nEnter task number to delete: "))
                if 1 <= task_num <= len(todo_list):
                    # Remove the item using its index position (minus 1 for python index mapping)
                    removed_item = todo_list.pop(task_num - 1)
                    print(f"🎉 Task '{removed_item}' marked as completed and removed!")
                else:
                    print("❌ Invalid number. Please pick a number from the list.")
            except ValueError:
                print("❌ Invalid input. Please type a valid number.")
                
    elif choice == "4":
        print("Exiting Task Manager. Goodbye and stay organized!")
        break
        
    else:
        print("❌ Invalid entry! Please enter a option between 1 and 4.")
