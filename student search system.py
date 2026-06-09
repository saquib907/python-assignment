student_list = ["saquib", "malhar", "aanya", "praneet"]
search_name = input("Enter student name to search: ")

# Check if item exists inside the list
if search_name in student_list:
    print("Student found in the database.")
else:
    print("Student not found.")