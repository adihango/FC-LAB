import datetime

def calculate_hours_worked(clock_in, clock_out):
    """Calculates the hours worked between clock-in and clock-out times."""
    clock_in_time = datetime.datetime.strptime(clock_in, "%H:%M")
    clock_out_time = datetime.datetime.strptime(clock_out, "%H:%M")
    hours_worked = clock_out_time - clock_in_time
    return hours_worked.total_seconds() / 3600

def analyze_attendance(employees):
    """Analyzes employee attendance data and provides insights."""
    total_hours_worked = {}
    perfect_attendance = []
    most_absences = []

    for employee in employees:
        total_hours = 0
        absences = 0
        for date, times in employee["attendance"].items():
            if times:
                hours_worked = calculate_hours_worked(times[0], times[1])
                total_hours += hours_worked
            else:
                absences += 1
        total_hours_worked[employee["employee_name"]] = total_hours
        if absences == 0:
            perfect_attendance.append(employee["employee_name"])
        if absences > 0:
            most_absences.append((employee["employee_name"], absences))

    # Find employee with the highest and lowest total hours
    highest_hours_employee = max(total_hours_worked, key=total_hours_worked.get)
    lowest_hours_employee = min(total_hours_worked, key=total_hours_worked.get)

    print("Total Hours Worked:")
    for employee, hours in total_hours_worked.items():
        print(f"{employee}: {hours} hours")

    print("\nEmployees with Perfect Attendance:")
    print(perfect_attendance)

    print("\nEmployees with the Most Absences:")
    most_absences.sort(key=lambda x: x[1], reverse=True)
    for employee, absences in most_absences:
        print(f"{employee}: {absences} absences")

    print("\nEmployee with the Highest Total Hours:")
    print(f"{highest_hours_employee}: {total_hours_worked[highest_hours_employee]} hours")

    print("\nEmployee with the Lowest Total Hours:")
    print(f"{lowest_hours_employee}: {total_hours_worked[lowest_hours_employee]} hours")

# Sample employee data
employees = [
    {"employee_name": "Rajesh Deshpande", "attendance": {"2024-08-15": ("09:00", "17:00"), "2024-08-16": ("09:15", "17:10")}},
    {"employee_name": "Amita Patil", "attendance": {"2024-08-15": ("09:30", "18:00"), "2024-08-16": ("09:00", "17:30")}},
    {"employee_name": "Rohit Sharma", "attendance": {"2024-08-15": ("09:00", "17:00"), "2024-08-16": None}}
]

analyze_attendance(employees)