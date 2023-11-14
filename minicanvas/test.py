from minicanvas import Ashesian, Faculty, Student, NotCanvas


# a1 = Ashesian("12342026", "Kofi Senam", "Ghanaian")
# print(a1)

# s1 = Student("12342026", "Richard Quayson", "Ghanaian", "CE", "2026", 2.0)
# print(s1)

# f1 = Faculty("23452020", "Dennis Owusu", "Ghanaian", "Computer Science and Information Systems")
# print(f1)

# print("\nAdding Ashesi Success to student1")
# s1.add_course("Asheesi Success")
# print(s1)

# print("\nChanging student1's name to Comfort")
# s1.change_name("Comfort Quayson")
# print(s1)

app = NotCanvas()
choice = app.menu()
while choice != "4":
    if choice == "1":
        app.register_student()
        print(app.students)
        
    elif choice == "2":
        app.register_faculty()
        
    else:
        print("Invalid choice!")
        
    choice = app.menu()