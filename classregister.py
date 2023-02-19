# import necessary modules
import uuid
import time

# list to store students
students = []

# A function to create student profile


def create_student(fname,lname):
    # student properties
    student = {
        "student_fname": fname,
        "student_lname": lname,
        "student_id": str(uuid.uuid4()),
    }

    # to add a student to the students list
    students.append(student)

# list to store the number of classes


classes = []
# A function to create class profile


def create_class(name, capacity, students_in_class):
    # class name should be unique
    for classs in classes:
        if classs["class_name"] == name:
            raise("class name should be unique")

    # class properties
    classs = {
        "class_name": name,
        "class_id": str(uuid.uuid4()),
        "class_capacity": capacity,
        "students_in_class": students_in_class
    }

    # to add a class in the classes list
    classes.append(classs)

# delete a class based on the class ID


def classs_delete(class_id):
    # intializes is_delete to false
    is_delete = False
    # deletes the class whose class ID has been passed
    for classs in classes:
        if classs["class_id"] == class_id:
            classes.remove(classs)
            is_delete = True
        # checks if the class has been deleted
        if is_delete == True:
            return("class has been deleted")
        else:
            return("class has not been deleted")

# deletes a student based on the student ID


def student_delete(student_id):
    # initialize stud_del to False
    stud_del = False
    # deletes the student whose student_id has been passed
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            stud_del = True
        # checks if the student has been deleted
        if stud_del == True:
            return("student has been deleted")
        else:
            return("student has not been deleted")

# list all the classes


def list_classes():
    return classes

# list all the students


def list_students():
    return students

# time log to start a class


def start_log(class_id):
    # initializes class start to False
    is_started = False
    # starts a class
    for classs in classes:
        if classs["class_id"] == class_id:
            start_time = time.time()
            is_started = True
        # checks if the class has started
        if is_started == True :
            return("class has started")
        else:
            return("class hasn't started")

# time log to end class


def end_log(class_id):
    # initialize class end to false
    is_ended = False
    # ends a class
    for classs in classes:
        if classs["class_id"] == class_id:
            end_time = time.time()
            is_ended = True
        # checks if the class has ended
        if is_ended == True:
            return("class has ended")
        else:
            return("class has ended")