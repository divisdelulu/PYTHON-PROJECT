import os

FILE_NAME = "students.txt"

# will read file/check if exists, if not will create one

def ensure_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            pass

# to add new Student to file

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{roll},{name},{marks}\n")

    print("\n Student added successfully!\n")


# to Display All Student in the file

def display_students():
    ensure_file()
    print("\n------ All Student Records ------")

    with open(FILE_NAME, "r") as f:
        data = f.readlines()

    if not data:
        print("No records found.")
    else:
        for line in data:
            roll, name, marks = line.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Marks: {marks}")

    print("--------------------------------\n")


# to Search Student by Roll Number

def search_student():
    roll_search = input("Enter roll number to search: ")
    found = False

    with open(FILE_NAME, "r") as f:
        for line in f:
            roll, name, marks = line.strip().split(",")
            if roll == roll_search:
                print(f"\nRecord Found!")
                print(f"Roll: {roll} | Name: {name} | Marks: {marks}\n")
                found = True
                break

    if not found:
        print("\nNo student found with that roll number.\n")



# to Delete Student from file

def delete_student():
    roll_delete = input("Enter roll number to delete: ")
    lines = []
    found = False

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    with open(FILE_NAME, "w") as f:
        for line in lines:
            roll, name, marks = line.strip().split(",")
            if roll == roll_delete:
                found = True
                continue 
            f.write(line)

    if found:
        print("\n Record deleted successfully!\n")
    else:
        print("\n No student found with that roll number.\n")
    
# Update Student deatails

def update_student():
    roll_update = input("Enter roll number to update: ")
    lines = []
    found = False

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    with open(FILE_NAME, "w") as f:
        for line in lines:
            roll, name, marks = line.strip().split(",")

            if roll == roll_update:
                print(f"\nCurrent -> Name: {name}, Marks: {marks}")
                name = input("Enter new name: ")
                marks = input("Enter new marks: ")
                f.write(f"{roll},{name},{marks}\n")
                print("\nRecord updated successfully!\n")
                found = True
            else:
                f.write(line)

    if not found:
        print("\n No student found with that roll number.\n")

# Main Menu

def menu():
    ensure_file()

    while True:
        print("========= STUDENT MANAGEMENT SYSTEM =========")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("\n Exiting the program. Goodbye!")
            break
        else:
            print("\n Invalid choice! Please try again.\n")

if __name__=="__main__":
    menu()
