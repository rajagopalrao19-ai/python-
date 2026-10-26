
timetable = [
    ("Python", "Monday", 9, 11, "Room A"),
    ("Maths", "Monday", 10, 12, "Room B"),
    ("Physics", "Tuesday", 9, 10, "Room C"),
    ("Chemistry", "Monday", 12, 13, "Room D")
]
available_rooms = ("Room A", "Room B", "Room C")
conflict = False
for i in range(len(timetable)):
    course1, day1, start1, end1, room1 = timetable[i]
    if room1 not in available_rooms:
        print(course1, "- Room unavailable:", room1)
        conflict = True
    for j in range(i + 1, len(timetable)):
        course2, day2, start2, end2, room2 = timetable[j]
        if day1 == day2 and start1 < end2 and start2 < end1:
            print("Timetable clash:", course1, "and", course2)
            conflict = True
if not conflict:
    print("Timetable is valid. No conflicts found.")
else:
    print("Proposed timetable is invalid.")
