# Student Management System

students = []  # List to store student records

# Function to add a student
def add_student():
    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))
    student = {"id": id, "name": name, "marks": marks}
    students.append(student)
    print("✅ Student added successfully!\n")

# Function to view all students
def view_students():
    if not students:
        print("⚠ No student records found.\n")
        return
    print("\n📋 Student Records:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Marks: {student['marks']}")
    print()

# Function to search a student by ID
def search_student():
    search_id = input("Enter Student ID to search: ")
    for student in students:
        if student["id"] == search_id:
            print(f"🔍 Found: ID: {student['id']}, Name: {student['name']}, Marks: {student['marks']}\n")
            return
    print("❌ Student not found.\n")

# Function to update a student
def update_student():
    update_id = input("Enter Student ID to update: ")
    for student in students:
        if student["id"] == update_id:
            student["name"] = input("Enter new name: ")
            student["marks"] = int(input("Enter new marks: "))
            print("✅ Student record updated!\n")
            return
    print("❌ Student not found.\n")

# Function to delete a student
def delete_student():
    delete_id = input("Enter Student ID to delete: ")
    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            print("🗑 Student record deleted!\n")
            return
    print("❌ Student not found.\n")

# Main menu loop
def menu():
    while True:
        print("📚 Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please try again.\n")

# Run the program
menu()

