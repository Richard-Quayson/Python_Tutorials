"""
How are we storing the data?

hostel_data = {
    hostel_name: rooms_data,
    hostel_name: rooms_data
}

Approach 1 (list in list):
rooms_data = [
    [room_number1, capacity, gender] // room 1
    [room_number2, capacity, gender] // room 2
    [room_number3, capacity, gender] // room 3
]

Approach 2 (list in dict):      ==>     Selected 👍👍
rooms_data = {
    room_number1: [capacity, gender] // room 2
    room_number2: [capacity, gender] // room 2
}

Approach 3: (dict in dict)
rooms_data = {
    room_number1: {
        capacity: capacity_value,
        gender: gender_value
    }

    room_number2: {
        capacity: capacity_value,
        gender: gender_value
    }
}

Final (list in dict in dict):
hostel_data = {
        hostel_name: {
        room_number1: [capacity, gender] // room 2
        room_number2: [capacity, gender] // room 2
    },

    hostel_name: {
        room_number1: [capacity, gender] // room 2
        room_number2: [capacity, gender] // room 2
    }
}

Future work:
- Abstraction of code into functions
- Read hostel data from file instead of using input
- Use object oriented approach
"""

# Abstraction is the idea of hiding unnecessary details.
# Keeping your code DRY. Avoid code repetition.

hostel_data = dict()

def menu():

    print("1. Give hostel information")
    print("2. Select room for a student")
    print("3. Exit")
    choice = input("What would you like to do? >>> ")
    print()

    return choice


def validate_num_rooms(num_rooms, hostel_name):
    # ensure num_rooms is a number
    while not num_rooms.isdigit():
        print(f"\n{num_rooms} is not a number.\n")
        num_rooms = input(f"How many rooms are in {hostel_name}? >>> ")

    return int(num_rooms)                  # convert num_rooms to integer


def validate_room_gender(room_gender, room_number):
    # ensure room_gender is a number
    while not room_gender.isdigit():
        print(f"\n{room_gender} is not a number.\n")
        room_gender = input(f"Is {room_number} a boy or girl's room?\n1. Boy \n2. Girl >>> ")
    
    return int(room_gender)


def validate_room_capacity(room_capacity, room_number):
    # ensure that room_capacity is a number
    while not room_capacity.isdigit():
        print(f"\n{room_capacity} is not a number.\n")
        room_capacity = input(f"How many people can be in {room_number}? >>> ")
            
    return int(room_capacity)      # convert room_capacity to integer


def collect_hostel_information():

    rooms_data = dict()
    # collect hostel information
    hostel_name = input("What is the name of the hostel? >>> ")
    num_rooms = input("How many rooms are in the hostel? >>> ")
    num_rooms = validate_num_rooms(num_rooms, hostel_name)

    for room in range(num_rooms):
        room_number = input(f"What is the room number for room {room + 1}? >>> ")
        room_capacity = input(f"How many people can be in {room_number}? >>> ")
        room_capacity = validate_room_capacity(room_capacity, room_number)

        room_gender = input(f"Is {room_number} a boy or girl's room?\n1. Boy \n2. Girl >>> ")
        room_gender = validate_room_gender(room_gender, room_number)

        if room_gender == 1:
            room_gender = "M"
        else:
            room_gender = "F"

        # store room_capacity and gender as a list with key room_number in rooms_data
        rooms_data[room_number] = [room_capacity, room_gender]
        print(rooms_data)

    hostel_data[hostel_name] = rooms_data
    print(hostel_data)


def room_allocation():
    
    print("Welcome to the Ashesi Housing Portal!")
    choice = menu()

    # convert choice to digit if number, else, request till it's a number
    while not choice.isdigit():
        print(f"\n{choice} is not a number.\n")
        choice = menu()

    choice = int(choice)

    while choice != 3:
        if choice == 1:
            collect_hostel_information()
        elif choice == 2:
            # select room
            pass
        else:
            print("Invalid choice!")
        print()

        print("Welcome to the Ashesi Housing Portal!")
        choice = menu()

        # convert choice to digit if number, else, request till it's a number
        while not choice.isdigit():
            print(f"{choice} is not a number.\n")
            choice = menu()

        choice = int(choice)

    print("Thanks for having you 😊!")

room_allocation()