def register_student(database):
    name = input("Enter student name: ")
    roll_number = input("Enter student roll number: ")
    password = input("Enter a password for the student: ")
    database[roll_number] = {'name': name, 'password': password, 'attendance': {}}
    save_database_to_file(database)  
    print("Student registered successfully!")

def view_student_database(database):
    if database:
        for roll_number, student_data in database.items():
            print(f"Roll Number: {roll_number}, Name: {student_data['name']}")
            print()
    else:
        print("No students are registered in the database.")

def delete_student_record(database):
    roll_number = input("Enter the roll number of the student to delete: ")
    if roll_number in database:
        del database[roll_number]
        save_database_to_file(database)  
        print("Student record deleted successfully!")
    else:
        print("Student not found in the database.")

def view_student_attendance(database):
    if database:
        roll_number = input("Enter your roll number: ")
        if roll_number in database:
            student_data = database[roll_number]
            print(f"Attendance for Roll Number {roll_number} - {student_data['name']}:")
            for date, status in student_data['attendance'].items():
                print(f"{date}: {'Present' if status == 'P' else 'Absent'}")
        else:
            print("Student not found in the database.")
    else:
        print("Database is empty!!!")

def mark_attendance(database):
    if database:
        roll_number = input("Enter your roll number: ")
        if roll_number in database:
            date = input("Enter the date (YYYY-MM-DD) for attendance: ")
            status = input("Enter 'P' for Present or 'A' for Absent: ").upper()
            if status == 'P':
                database[roll_number]['attendance'][date] = 'P'
                save_database_to_file(database)  
                print("Attendance marked as Present.")
            elif status == 'A':
                database[roll_number]['attendance'][date] = 'A'
                save_database_to_file(database)  
                print("Attendance marked as Absent.")
            else:
                print("Invalid input! Please enter 'P' for Present or 'A' for Absent.")
        else:
            print("Student not found in the database.")
    else:
        print("Database is empty!!!")
