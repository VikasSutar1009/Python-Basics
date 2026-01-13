students = {}


def add_student(roll, name, marks):
    students[roll] = {"name": name, "marks": marks}

def view_students():
    for k, v in students.items():
        print(k, v)

add_student(101, "Amit", 85)
add_student(102, "Riya", 90)
view_students()