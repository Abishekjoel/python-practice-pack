# def main():
#     todo_list = []
#     todo_list.append(str(input("Enter task: ").strip().capitalize()))
#     try:
#         action = ""
#         while action != "q":
#             print("-------- TODO LIST --------\n")
#             for index, todo in enumerate(todo_list, start=1):
#                 print(f"Task {index}. {todo}")
#                 print("--------------------------\n")
#             action = str(input("Enter add to add task, edit to edit, or del to delete and q to quit:\n")).strip().lower()
#             if action == "add":
#                 todo_list.append(str(input("Enter task: ").strip().capitalize()))
#             elif action == "edit":
#                 edit_id = int(input("Enter id to edit: ")) - 1
#                 todo_list[edit_id] = str(input("Enter edit value: "))
#             elif action == "del":
#                 todo_list.pop(int(input("Enter the id to delete: ")) - 1)
#             elif action == "q":
#                 pass
#             else:
#                 print("Enter valid action")
#     except :
#         main()

# main()

todo_list = []

def getInput():
    todo_list.append(str(input("Enter task: ").strip().capitalize()))

def show():
    print("-------- TODO LIST --------\n")
    for index, todo in enumerate(todo_list, start=1):
        print(f"Task {index}. {todo}")
    print("--------------------------\n")

def delete():
    todo_list.pop(int(input("Enter the id to delete: ")) - 1)

def edit():
    edit_id = int(input("Enter id to edit: ")) - 1
    todo_list[edit_id] = str(input("Enter edit value: "))

def action_input():
    return str(input("Enter add to add task, edit to edit, or del to delete and q to quit:\n")).strip().lower()


def main():
    getInput()
    try:
        action = ""
        while action != "q":
            show()
            action = action_input()

            if action == "add":
                getInput()
            elif action == "edit":
                edit()
            elif action == "del":
                delete()
            else:
                print("Enter valid action")
    except:
        print("Enter valid action")
        main()

main()
