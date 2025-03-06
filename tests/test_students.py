import unittest
from exceptions.exception import NotFoundException, EmailAlreadyExistException, NameAlreadyExistException
from src.Students import Students
from src.student import Student
from src.course import Course
from src.grade import Grade
from src.teacher import Teacher

class TestStudents(unittest.TestCase):

    def setUp(self):
        self.students_manager = Students()
        self.student1 = Student("John Doe", "john.doe@example.com", "password123")
        self.student2 = Student("Jane Smith", "jane.smith@example.com", "password456")
        self.course1 = Course("CS101", "Introduction to Computer Science")
        self.course2 = Course("MATH101", "Introduction to Mathematics")

    def test_add_student(self):
        self.students_manager.add_student(self.student1)
        self.assertEqual(len(self.students_manager.get_all_students()), 1)

        with self.assertRaises(EmailAlreadyExistException):
            self.students_manager.add_student(Student("Another John", "john.doe@example.com", "password789"))

        with self.assertRaises(NameAlreadyExistException):
            self.students_manager.add_student(Student("John Doe", "another.john@example.com", "password789"))

    def test_remove_student(self):
        self.students_manager.add_student(self.student1)
        self.students_manager.remove_student("john.doe@example.com")
        self.assertEqual(len(self.students_manager.get_all_students()), 0)

        with self.assertRaises(NotFoundException):
            self.students_manager.remove_student("non.existent@example.com")