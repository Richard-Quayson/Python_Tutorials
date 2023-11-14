class Ashesian:
    
    def __init__(self, ID, name, nationality):
        self.id = ID
        self.name = name
        self.courses = []
        self.nationality = nationality
        
    def __str__(self):
        return f"Ashesian = ID: {self.id}, Name: {self.name}"
        

class Student(Ashesian):
    
    def __init__(self, ID, name, nationality, major, year_group, gpa=4.0):
        super().__init__(ID, name, nationality)
        self.major = major
        self.gpa = gpa
        self.year_group = year_group
        
    def __str__(self):
        return f"Student = ID: {self.id}, Name: {self.name}, Nationality: {self.nationality}, Year Group: {self.year_group} Major: {self.major}, Courses: {self.courses}"
        # return "ID: (), Name: (), Major: (), Courses: ()".format(self.id, self.name, self.major, self.courses)
        
    def add_course(self, course_name):
        self.courses.append(course_name)
        
    def change_name(self, new_name):
        self.name = new_name
        
        
class Faculty(Ashesian):
    
    def __init__(self, ID, name, nationality, department):
        super().__init__(ID, name, nationality)
        self.department = department
        self.certifications = []
        
    def __str__(self):
        return f"Faculty = ID: {self.id}, Name: {self.name}, Courses: {self.courses}, Department: {self.department}, Certifications: {self.certifications}"
        
        
class NotCanvas:
    
    def __init__(self):
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
    

if __name__ == "__main__":
    a1 = Ashesian("12342026", "Kofi Senam", "Ghanaian")
    print(a1)

    s1 = Student("12342026", "Richard Quayson", "Ghanaian", "CE", "2026", 2.0)
    print(s1)

    f1 = Faculty("23452020", "Dennis Owusu", "Ghanaian", "Computer Science and Information Systems")
    print(f1)

    print("\nAdding Ashesi Success to student1")
    s1.add_course("Asheesi Success")
    print(s1)

    print("\nChanging student1's name to Comfort")
    s1.change_name("Comfort Quayson")
    print(s1)