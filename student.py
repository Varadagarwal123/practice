def view_my_attendance(database, roll_number):
    if database:
        if roll_number in database:
            student_data = database[roll_number]
            print(f"Attendance for Roll Number {roll_number} - {student_data['name']}:")
            for date, status in student_data['attendance'].items():
                print(f"{date}: {'Present' if status == 'P' else 'Absent'}")
        else:
            print("Student not found in the database.")
    else:
        print("Database is empty!!!")