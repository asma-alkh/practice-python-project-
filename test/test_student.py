import unittest
from student.student import Student 

class TestStudent(unittest.TestCase):

    def test_create_student_object(self):
        new_student = Student('Asma')
        self.assertEqual(new_student.name, 'Asma')