# import necessary modules
import uuid
import time
from datetime import datetime
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


def create_class(name, capacity):
    # class name should be unique
    for classs in classes:
        if classs["class_name"] == name:
            raise("class name should be unique")



    # class properties
    classs = {
        "class_name": name,
        "class_id": str(uuid.uuid4()),
        "class_capacity": capacity,
        "start_time": None,
        "end_time": None
    }

    # to add a class in the classes list
    classes.append(classs)

#to find a class using its id
def find_class_by_ID(class_id):
    is_found = False
    class_ = None
    for classs in classes:
        if classs["class_id"] == class_id:
            class_ = classs
            is_found = True
            break
    return class_,is_found


# delete a class based on the class ID
def classs_delete(class_id):
    # intializes is_delete to false
    is_delete = False
    # deletes the class whose class ID has been passed
    class_,is_found = find_class_by_ID(class_id)
    if not is_found:
        raise("class matching id not found")
    classes.remove(class_)
    is_delete = True

# deletes a class based on the student ID
    if is_delete == True:
        return ("the class has been deleted")

def find_student_by_ID(student_id):
    is_student_found = False
    student_ = None
    #finds a student with his id
    for student in students:
        if student["student_id"] == student_id:
            student_ = student
            is_student_found = True
            break

    return student_,is_student_found

def student_delete(student_id):
    # initialize stud_del to False
    stud_del = False
    # deletes the student whose student_id has been passed
    student_,is_student_found = find_student_by_ID(student_id)
    if not is_student_found:
        raise("student matching student id not found")
    #deletes the student matching student id
    students.remove(student_)
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
    class_,is_found = find_class_by_ID(class_id)
    if not is_found:
        raise("class matching id not found")

    class_["start_time"] = datetime.now()
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
