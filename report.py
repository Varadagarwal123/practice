import datetime
def generate_daily_report(database):
    if database:
        date = input("Enter the date (YYYY-MM-DD) for the daily report: ")
        report_filename = f"daily_report_{date}.txt"
        with open(report_filename, 'w') as file:
            file.write("Daily Report:\n")
            for roll_number, student_data in database.items():
                name = student_data['name']
                attendance = student_data['attendance']
                present = date in attendance and attendance[date] == 'P'
                file.write(f"Name: {name}, Roll Number: {roll_number}, Attendance: {'Present' if present else 'Absent'}\n")
        print(f"Daily report generated and saved as '{report_filename}'.")
    else:
        print("Database is empty!!!")

def generate_weekly_report(database):
    if database:
        week_start_date = input("Enter the start date (YYYY-MM-DD) of the week for the weekly report: ")
        report_filename = f"weekly_report_{week_start_date}.txt"

        with open(report_filename, 'w') as file:
            file.write("Weekly Report:\n")
            for roll_number, student_data in database.items():
                name = student_data['name']
                attendance = student_data['attendance']
                week_end_date = datetime.datetime.strptime(week_start_date, '%Y-%m-%d') + datetime.timedelta(days=6)
                week_end_date_str = week_end_date.strftime('%Y-%m-%d')
                total_attendance = sum(week_start_date <= date <= week_end_date_str and attendance[date] == 'P' for date in attendance)

                file.write(f"Name: {name}, Roll Number: {roll_number}, Attendance: {total_attendance} days\n")

        print(f"Weekly report generated and saved as '{report_filename}'.")
    else:
        print("Database is empty!!!")


def generate_monthly_report(database):
    if database:
        month = input("Enter the month (YYYY-MM) for the monthly report: ")
        report_filename = f"monthly_report_{month}.txt"
        with open(report_filename, 'w') as file:
            file.write("Monthly Report:\n")
            for roll_number, student_data in database.items():
                name = student_data['name']
                attendance = student_data['attendance']
                present_count = sum(date.startswith(month) and attendance[date] == 'P' for date in attendance)
                file.write(f"Name: {name}, Roll Number: {roll_number}, Attendance: {present_count} days\n")
        print(f"Monthly report generated and saved as '{report_filename}'.")
    else:
        print("Database is empty!!!")