# ---------------------------------

# File          : python_variables.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 08/10/2021
# Modified Date : 08/10/2021
# Description   : Testing the functionality of List, Tuples
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

if __name__ == "__main__":

    x = input("Enter the L-Number1 : ")
    # Taking First L-Number as the input

    print(" The L-number you have entered is : "+x)

    y = input("Enter the L-number2 : ")
    # Taking First L-Number as the input

    print(" The L-number you have entered is : " + y)
    tuple_test = (x, y)
    # Tuple list of 2 fake Lnumbers for students
    module_list = ["Java_ooprogramming","Python_Scripting"]
    # List of 2 module subjects to be assigned to the students

    # print(tuple_test)
    # print(module_list)
    # To check the intermiediate solution

    # Printing tuple lists for check

    student1_details = {x:module_list}
    student2_details = {y:module_list}
    # Dictionary for L number and module list

    java_stud1 = {x: 40}
    java_stud2 = {y: 70}
    # Dictionary for L number and Java grade for both students

    python_stud1 = {x: 69}
    python_stud2 = {y: 58}
    # Dictionary for L number and python grade for both students

    print("\n")


    print("Student 1 grades : ")
    print(java_stud1)
    print(python_stud1)
    # returns Student 1 grades

    print(student1_details)

    # Printing grade details of Student 1

    print("\n")

    # Printing grade details of Student 2

    print("Student 2 grades : ")
    print(java_stud2)
    print(python_stud2)

    # returns Student 2 grades

    print(student2_details)

    print("\n")
print("Thank you for using my application")

# End of the code