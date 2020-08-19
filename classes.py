# Udemy Python Review 
# 8/17/2020

class Student:
	def __init__(self, name, grades):
		self.name = name
		self.grades = grades

	def average_grade(self):
		return sum(self.grades) / len(self.grades)

student = Student("Frank", (99, 83, 94, 88))
student_2 = Student("Rolf", (99, 93, 94, 88))


print(student.average_grade())
print(student.name)

print(student_2.average_grade())
print(student_2.name)

class Person:
	def __init__(self, name, age):
		self.name = name 
		self.age = age

	# Called when wanting to turn method into string
	def __str__(self):
		return f"Person {self.name}, {self.age} years old"

	# Print out unambigous representation of an object
	def __repr__(self):
		return f"<Person {self.name}, {self.age}>"

bob = Person("Bob", 34)
print(bob)
print(bob.__repr__())




# Class Methods
class Book:
	TYPES = ("hardcover", "paperback")

	def __init__(self, name, book_type, weight):
		self.name = name 
		self.book_type = book_type
		self.weight = weight

	def __repr__(self):
		return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

	@classmethod
	def hardcover(cls, name, page_weight):
		return cls(name, cls.TYPES[0], page_weight + 100)

	@classmethod
	def paperback(cls, name, page_weight):
		return cls(name, cls.TYPES[1], page_weight)

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print (book) 
print (light)
print()

import functools

# decorators 
user = {"username" : "Rolf", "access_level" : "guest"}

def make_secure(access_level):
	def decorator(func):
		@functools.wraps(func)
		def secure_function(*args, **kwargs):
			if user["access_level"] == access_level:
				return func(*args, **kwargs)
			else:
				return f"No {access_level} permissions for {user['username']}."

		return secure_function

	return decorator

@make_secure("admin")
def get_admin_password():
	return "admin: 1234" 

@make_secure("user")
def get_dashboard_password():
	return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())
print()

user = {"username" : "anna", "access_level" : "admin"}

print(get_admin_password())
print(get_dashboard_password())
print()