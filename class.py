class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

        Student.count += 1
        Student.total_gpa += gpa

    #instance method
    def get_info(self):
        return f"{self.name}, {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {Student.count}"

    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA { Student.total_gpa/cls.count :}"

student1 = Student("Tom", 96)
student2 = Student("Aspinal", 87)
student3 = Student("Take", 79)

print(Student.get_count())
print(Student.average_gpa())

