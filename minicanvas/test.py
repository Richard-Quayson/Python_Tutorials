from minicanvas import Ashesian, Faculty, Student, NotCanvas


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