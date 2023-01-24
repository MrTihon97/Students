students = {
}
tasks = []
names = []
def add_student(student):
    global students
    if student not in names:
        names.append(student)
        students[student] = {}

def add_class(task):
    global students
    if task not in tasks:
        tasks.append(task)
        for name in names:
            students[name][task]=[]

def add_mark(student,task,mark):
    global students
    students[student][task].append(mark)


