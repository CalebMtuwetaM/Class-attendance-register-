import classregister

# create a student
classregister.create_student("Caleb","Mtuweta")
classregister.create_student("Hope","Esther")
classregister.create_student("Mweni","Munira")
classregister.create_student("Ivy","Wangari")
classregister.create_student("Trevor","Kianga")

# giving students variables
stud1 = classregister.students[0]
stud2 = classregister.students[1]
stud3 = classregister.students[2]
stud4 = classregister.students[3]
stud5 = classregister.students[4]

# create a class
classregister.create_class("form 1","10","6")
classregister.create_class("form 2","10","6")
classregister.create_class("form 3","10","6")
classregister.create_class("form 4","10","6")
classregister.create_class("form 5","10","6")

# giving classes variables
class1 = classregister.classes[0]
class2 = classregister.classes[1]
class3 = classregister.classes[2]
class4 = classregister.classes[3]
class5 = classregister.classes[4]

# to view the class list
#print(classregister.list_classes())

# to view students list
#print(classregister.list_students())

# to remove a class
#print(classregister.classs_delete(class1["class_id"]))

# to remove a student 
#print(classregister.student_delete(stud1["student_id"]))

# to start a class
#print(classregister.start_log(class1["class_id"]))

# to end a class 
#print(classregister.end_log(class1["class_id"]))