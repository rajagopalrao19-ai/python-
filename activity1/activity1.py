
courses = [
    ("Python", 40, "9AM"),
    ("Maths", 30, "10AM"),
    ("Physics", 50, "9AM")
]
rooms = [
    ("Room A", 45),
    ("Room B", 60)
]
timetable = []
allocated_courses = []

for course in courses:
    name, students, period = course
    assigned = False

    for room in rooms:
        room_name, capacity = room

        if capacity >= students:

            clash = False

            for entry in timetable:
                if entry[0] == room_name and entry[1] == period:
                    clash = True
                    break

            if not clash:
                timetable.append((room_name, period, name))
                allocated_courses.append(name)
                assigned = True
                break

    if not assigned:
        print("Cannot allocate:", name)

print("\n--- Smart Classroom Timetable ---")

for entry in timetable:
    print("Room:", entry[0],
          "| Period:", entry[1],
          "| Course:", entry[2])

if len(allocated_courses) == len(courses):
    print("\nAll courses accommodated successfully!")
else:
    print("\nAll courses cannot be accommodated.")
    print("Allocated:", len(allocated_courses))
    print("Total courses:", len(courses))
