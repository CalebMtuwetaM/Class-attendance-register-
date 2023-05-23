# import all necessary modules 
import unittest
import class_register

class TestClassRegister(unittest.TestCase):
    # set up function to set the test data
    class_register.create_class("west","20")
    class2 = class_register.classes[-1]
    # happy path test for create_class function 
    def happy_path_for_create_class(self):
        is_created = False 
        class_register.create_class("classA","10")
        class1 = class_register.classes[0]
        is_created = True
        if is_created == False:
            self.assertRaises(ValueError)

    # happy path test for create_student function 
    def happy_path_for_create_student(self):
        is_stud_created = False
        class_register.create_student("Steve","mukala")
        stud7 = class_register.students[0]
        is_stud_created = True
        if is_stud_created == False:
            self.assertRaises(ValueError)

    # happy path test for find class by id 
    def happy_path_test_for_find_class_by_id(self):
        is_found = False
        id = class2["class_id"]
        class_register.find_class_by_ID(class2["class_id"])
        is_found = True
        if is_found == False:
            self.assertRaises (ValueError)

    # happy path test for delete class 
    def happy_path_test_for_delete_class(self):
        is_deleted = False
        class_register.create_student("Carlos","nkatha")
        stud8 = class_register.students[-1]
        class_register.classs_delete(stud8["class_id"])
        is_deleted = True
        if is_deleted == False:
            self.assertRaises (ValueError)
            

if __name__ == '__main__':
    unittest.main()