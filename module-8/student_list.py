import json


def print_students(student_list):
    """Print each student's information."""
    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        )


# Load the JSON file
with open("Student.json", "r") as file:
    students = json.load(file)

print("Original Student List")
print("---------------------")
print_students(students)

# Add your information
new_student = {
    "F_Name": "Luis",
    "L_Name": "Rodriguez",
    "Student_ID": 951753,
    "Email": "lrodriguez@email.com"
}

students.append(new_student)

print("\nUpdated Student List")
print("---------------------")
print_students(students)

# Save the updated JSON file
with open("Student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nThe student.json file has been updated.")
