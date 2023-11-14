class Ashesian:
    
    def _init_(self, ID, name, nationality):
        self.id = ID
        self.name = name
        self.courses = []
        self.nationality = nationality
        
    def _str_(self):
        return f"Ashesian = ID: {self.id}, Name: {self.name}"
        

class Student(Ashesian):
    
    def _init_(self, ID, name, nationality, major, year_group, gpa=4.0):
        super()._init_(ID, name, nationality)
        self.major = major
        self.gpa = gpa
        self.year_group = year_group
        
    def _str_(self):
        return f"Student = ID: {self.id}, Name: {self.name}, Nationality: {self.nationality}, Year Group: {self.year_group} Major: {self.major}, Courses: {self.courses}"
        # return "ID: (), Name: (), Major: (), Courses: ()".format(self.id, self.name, self.major, self.courses)
        
    def add_course(self, course_name):
        self.courses.append(course_name)
        
    def change_name(self, new_name):
        self.name = new_name
        
        
class Faculty(Ashesian):
    
    def _init_(self, ID, name, nationality, department):
        super()._init_(ID, name, nationality)
        self.department = department
        self.certifications = []
        
    def _str_(self):
        return f"Faculty = ID: {self.id}, Name: {self.name}, Courses: {self.courses}, Department: {self.department}, Certifications: {self.certifications}"
        
        
class NotCanvas:
    
    def _init_(self):
        self.students = []
        self.faculty = []
        self.courses = []
        
    def register_student(self):
        id = int(input("ID: "))
        name = input("Name: ")
        major = input("Major: ")
        nationality = input("Nationality: ")
        year_group = input("Year Group: ")
        
        student = Student(id, name, nationality, major, year_group)
        self.students.append(student)
        
    def menu(self):
        print("\nWelcome to NotCanvas")
        print("1. Register Student")
        print("2. Register Faculty")
        print("3. View Students")
        print("4. Exit")
        choice = input("What would you like to do? ")
        return choice