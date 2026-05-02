Tasks ={}
task_number = 1

while True:
    try:
        number = int(input(""" \nEnter the task number:
    1| Add Task
    2| View Task List
    3| View Task
    4| Mark Task as Done
    5| Exit
    """))

        if number == 1:
            task = input("Enter task: ")
            Tasks[task_number] = {"task": task , "done" : False}
            task_number += 1 
            print(Tasks)

        elif number == 2:
            print(Tasks)

        elif number == 3: 
            if not Tasks:
                print("No tasks available")
            else:
                for task_detail, info in Tasks.items():
                    status = "✔️" if info["done"] else "❌"
                    print(f"{task_detail}: {info['task']}: {status} ")

        elif number == 4:
            if not Tasks:
                print("No tasks to mark.")
            else:
                for num, info in Tasks.items():
                    status = "✔️" if info["done"] else "❌"
                    print(f"{num}. {info['task']} {status}")

                task_done = int(input("Enter task number to mark as done: "))
                
                if task_done in Tasks:
                    Tasks[task_done]["done"] = True
                else:
                    print("Invalid task number.")
        
        elif number == 5:
            print("Exiting the Program...")
            break

        else:
            print("Invalid Choice amongs the options")


    except ValueError:
        print("Please enter a valid number")
