class Student:
    #store a student's name and list of grades 
    def __init__(self, name):
        self.name = name 
        self.grade = []

if  __name__ == '__main__':      
    student_name = input('Enter the new student name: ')
    
    new_student = Student(student_name)
    print(f'Welcome {new_student.name}')