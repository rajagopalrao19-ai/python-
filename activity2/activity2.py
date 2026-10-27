
students = {
    "Ravi": {
        "Python": [50, 65, 80],
        "Maths": [70, 60, 55],
        "Physics": [45, 50, 60]
    },
    "Sita": {
        "Python": [80, 85, 90],
        "Maths": [75, 80, 85],
        "Physics": [70, 75, 80]
    }
}

for name, subjects in students.items():
    print("\nStudent Name:", name)
    total = 0
    count = 0
    weak_subjects = []

    for subject, marks in subjects.items():
        improvement = marks[-1] - marks[0]
        average = sum(marks) / len(marks)
        total += average
        count += 1

        print("\nSubject:", subject)
        print("Exam Marks:", marks)
        print("Improvement/Decline:", improvement)

        if average < 50:
            weak_subjects.append(subject)

    overall_average = total / count
    print("\nOverall Average:", round(overall_average, 2))

    if weak_subjects:
        print("Weak Subjects:", ", ".join(weak_subjects))
    else:
        print("Weak Subjects: None")

    if overall_average >= 75:
        print("Classification: Excellent")
    elif overall_average >= 60:
        print("Classification: Good")
    elif overall_average >= 40:
        print("Classification: Average")
    else:
        print("Classification: Needs Improvement")
