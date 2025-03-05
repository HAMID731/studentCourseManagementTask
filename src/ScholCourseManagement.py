def get_choice(prompt):
    while True:
        choice = input(prompt)
        return choice

def student_menu():
    while True:
        print("""
        1. View Notification
        2. Register Course
        3. View Grade
        4. Exit
        """)
        choice = get_choice("Enter your choice: ")
        match choice:
            case "1":
                print("Notification viewed")
            case "2":
                print("Registered successfully")
            case "3":
                print("View grades already")
            case "4":
                print("Exiting student menu...")
                return
            case _:
                print("Invalid choice. Please try again.")

def teacher_menu():
    while True:
        print("""
        1. Create Course
        2. Assign Grades
        3. Send Notification
        4. Exit
        """)
        choice = get_choice("Enter your choice: ")
        match choice:
            case "1":
                print("Create course successfully")
            case "2":
                print("Already Assign Grades")
            case "3":
                print("Notification sent successfully")
            case "4":
                print("Exiting teacher menu...")
                return
            case _:
                print("Invalid choice. Please try again.")

def register_student():
    s_name = input("Enter your name: ")
    email = input("Enter your email: ")
    set_password = input("Set Strong password: ")
    print("Registered successfully as a student.")
    main_menu()

def register_teacher():
    t_name = input("Enter your name: ")
    t_email = input("Enter your email: ")
    set_t_password = input("Set Strong password: ")
    print("Registered successfully as a teacher.")
    main_menu()

def login_student():
    s_email = input("Enter your email: ")
    s_password = input("Enter your password: ")
    print("Login successful as a student.")
    student_menu()

def login_teacher():
    t_email = input("Enter your email: ")
    t_password = input("Enter your password: ")
    print("Login successful as a teacher.")
    teacher_menu()

def main_menu():
    while True:
        print("""\nWelcome to the STUDENT COURSE MANAGEMENT!
        1. Register
        2. Login
        3. Exit
        """)
        choice = get_choice("Enter your choice: ")
        match choice:
            case "1":
                print("""
                1. Register as Student
                2. Register as Teacher
                3. Exit
                """)
                register_choice = get_choice("Enter your choice: ")
                match register_choice:
                    case "1":
                        register_student()
                    case "2":
                        register_teacher()
                    case "3":
                        print("Exiting registration...")
                        return
                    case _:
                        print("Invalid choice. Please try again.")
            case "2":
                print("""
                1. Login as Student
                2. Login as Teacher
                3. Exit
                """)
                login_choice = get_choice("Enter your choice: ")
                match login_choice:
                    case "1":
                        login_student()
                    case "2":
                        login_teacher()
                    case "3":
                        print("Exiting login...")
                        return
                    case _:
                        print("Invalid choice. Please try again.")
            case "3":
                print("Exiting the program. Goodbye!")
                return
            case _:
                print("Invalid choice. Please try again.")

def main():
    main_menu()

if __name__ == "__main__":
    main()