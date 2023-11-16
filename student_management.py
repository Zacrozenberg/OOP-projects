class Student:
    number_of_students = 0
    students = []

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        Student.number_of_students += 1
        Student.students.append(self)

    def __repr__(self):
        return f"Student('{self.name}', '{self.age}', '{self.course}')"

    def __str__(self):
        return f"{self.name} - {self.age} years old - enrolled in {self.course} - {self.email}"

    @property
    def email(self):
        return f'{self.name}.{self.course}@university.com'


class StudentManager:
    def __init__(self, students=None):
        if students is not None:
            self.students = students
            self.number_of_students = len(students)
        else:
            self.students = []
            self.number_of_students = 0

    def add_student(self, student):
        self.students.append(student)
        self.number_of_students += 1

    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                self.number_of_students -= 1
                return
            else:
                print(f"Student '{student_name}' not found. \n")

    def display_students(self):
        print(f'{self.number_of_students} currently enrolled: \n')
        for student in self.students:
            print(student)
        print('\n')


if __name__ == '__main__':
    student1 = Student('Tal Knino', 30, 'HR')
    student2 = Student('Zac Rozenberg', 29, 'Electrical Engineering')

    studentmanager = StudentManager([student1])
    studentmanager.display_students()

    studentmanager.add_student(student2)
    studentmanager.display_students()

    studentmanager.remove_student('Tal Knino')
    studentmanager.display_students()
