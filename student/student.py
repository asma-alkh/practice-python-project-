class Student:
    #store a student's name and list of grades 
    def __init__(self, name):
        self.name = name 
        self.grades = []
    def add_grade(self, grade):
        # method to add a grade (0 to 100 only). invalid grades should raise error.
        if grade >= 0 and grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError('Grade must be between 0 and 100 inclusive')    
    def average(self):
        if not self.grades:
            return 0

        total = 0
        for grade in self.grades:
            total += grade
        average = total / len(self.grades)
        return average        



if  __name__ == '__main__':      
    student_name = input('Enter the new student name: ')
    new_student = Student(student_name)
    print(f'Welcome {new_student.name}')
    new_grade = input('Add grade to student: ')
    try:
        new_student.add_grade(int(new_grade))
    except ValueError as err:
        print(err)    
