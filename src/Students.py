from exceptions.exception import NotFoundException, EmailAlreadyExistException, VerificationFailedException, \
    NameAlreadyExistException
from src.grade import Grade
from src.student import Student
from src.course import Course
from src.teacher import Teacher


class Students:
    def __init__(self):
        self.__students = []

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError("Expected a Student object.")

        for existing_student in self.__students:
            if existing_student.email == student.email:
                raise EmailAlreadyExistException("Email already registered.")
            if existing_student.name == student.name:
                raise NameAlreadyExistException("Name already registered.")

        self.__students.append(student)

    def remove_student(self, email: str):
        student = self.find_student_by_email(email)
        if student:
            self.__students.remove(student)
        else:
            raise NotFoundException("Student not found.")




