
students = []

print("Welcome to Student Data Organizer!")
print()

while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        
        case 1:
            print("\nEnter student details:")
            student_id = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ")

            student = {
                "Student_id": student_id,
                "Name": name,
                "Age": age,
                "Grade": grade,
                "Date_of_Birth": dob,
                "Subjects": subjects
            }

            students.append(student)
            print("Student added successfully!\n")

        
        case 2:
            print("\n--- Display All Students ---")
            if not students:
                print("No students found.\n")
            else:
                for stu in students:
                    print(
                        f"ID: {stu['Student_id']} | "
                        f"Name: {stu['Name']} | "
                        f"Age: {stu['Age']} | "
                        f"Grade: {stu['Grade']} | "
                        f"Subjects: {stu['Subjects']}"
                    )
                print()

        
        case 3:
            sid = int(input("Enter Student ID to update: "))
            found = False

            for stu in students:
                if stu["Student_id"] == sid:
                    found = True

                    print("1. Update Name")
                    print("2. Update Age")
                    print("3. Update Grade")
                    print("4. Update Subjects")

                    op = int(input("Enter operation: "))

                    match op:
                        case 1:
                            stu["Name"] = input("Enter new name: ")
                        case 2:
                            stu["Age"] = int(input("Enter new age: "))
                        case 3:
                            stu["Grade"] = input("Enter new grade: ")
                        case 4:
                            stu["Subjects"] = input("Enter new subjects: ")
                        case _:
                            print("Invalid operation")

                    print("Student information updated!\n")
                    break

            if not found:
                print("Student ID not found.\n")

        
        case 4:
            sid = int(input("Enter Student ID to delete: "))
            found = False

            for stu in students:
                if stu["Student_id"] == sid:
                    students.remove(stu)
                    found = True
                    print("Student deleted successfully!\n")
                    break

            if not found:
                print("Student ID not found.\n")

        
        case 5:
            print("\n--- Offered Subjects List ---")
            if not students:
                print("No subjects available.\n")
            else:
                for stu in students:
                    print(stu["Subjects"])
                print()

       
        case 6:
            print("Program Exit`ed !!!")
            break

        case _:
            print("Invalid choice")

          
            

























                    
                    
            
            

        
            
