# Write a program to manage information of student. The program implements terminology of OOP paradigm.
# A student information consists of ID, Student Name, Semester, Course Name.
# The program allows use to create list of student, update/delete student information. On the other hand,
# use can search student(s) and sort result by student name.
# Main Screen as below:
# WELCOME TO STUDENT MANAGEMENT
# 1. Create
# 2. Find and Sort
# 3. Update/Delete
# 4. Report
# 5. Exit

class Student:
    _next_id = 1

    def __init__(self, name, semester, course):
        self._id = Student._next_id
        Student._next_id += 1
        self._name = name
        self._semester = semester
        self._course = course

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, value):
        self._semester = value

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Semester: {self._semester}, Course: {self._course}"


class StudentManagement:
    def __init__(self):
        self._students = []

    def create_student(self):
        name = input("Enter student name: ")
        semester = input("Enter semester: ")
        course = input("Enter course name: ")
        student = Student(name, semester, course)
        self._students.append(student)
        print("Student created successfully.")

    def find_and_sort(self):
        search_name = input("Enter student name to search: ")
        found_students = [student for student in self._students if search_name.lower() in student.name.lower()]
        found_students.sort(key=lambda student: student.name)
        for student in found_students:
            print(student)
        if not found_students:
            print("No student found.")

    def update_or_delete(self):
        student_id = int(input("Enter student ID to update/delete: "))
        student = next((student for student in self._students if student.id == student_id), None)
        if student:
            print(f"1. Update\n2. Delete\n3. Cancel")
            choice = input("Enter your choice: ")
            if choice == '1':
                student.name = input("Enter new student name: ")
                student.semester = input("Enter new semester: ")
                student.course = input("Enter new course name: ")
                print("Student updated successfully.")
            elif choice == '2':
                self._students.remove(student)
                print("Student deleted successfully.")
        else:
            print("Student not found.")

    def report(self):
        for student in self._students:
            print(student)
        if not self._students:
            print("No student to display.")

    def exit(self):
        print("Exiting the program.")
        exit()

    def main_menu(self):
        while True:
            print("WELCOME TO STUDENT MANAGEMENT")
            print("1. Create")
            print("2. Find and Sort")
            print("3. Update/Delete")
            print("4. Report")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_student()
            elif choice == '2':
                self.find_and_sort()
            elif choice == '3':
                self.update_or_delete()
            elif choice == '4':
                self.report()
            elif choice == '5':
                self.exit()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    management = StudentManagement()
    management.main_menu()


