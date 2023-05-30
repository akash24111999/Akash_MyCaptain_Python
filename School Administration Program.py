class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def display_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("List of students:")
            for student in self.students:
                print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")


def main():
    school = School()

    while True:
        print("\nSchool Administration Program")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")

            student = Student(name, age, grade)
            school.add_student(student)
            print("Student added successfully.")

        elif choice == '2':
            name = input("Enter student name to remove: ")

            for student in school.students:
                if student.name == name:
                    school.remove_student(student)
                    print("Student removed successfully.")
                    break
            else:
                print("Student not found.")

        elif choice == '3':
            school.display_students()

        elif choice == '4':
            print("Quitting the program...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
