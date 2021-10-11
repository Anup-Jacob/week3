# ---------------------------------

# File          : python_variables.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 08/10/2021
# Modified Date : 09/10/2021
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
    #tuple_test = (x, y)
    # Tuple list of 2 fake Lnumbers for students
    #module_list = ["Java_ooprogramming","Python_Scripting"]
    # List of 2 module subjects to be assigned to the students

    # print(tuple_test)
    # print(module_list)
    # To check the intermiediate solution

    # Printing tuple lists for check

    #student1_details = {x:module_list}
    #student2_details = {y:module_list}
    # Dictionary for L number and module list

    #java_stud1 = {x: 40}
    #java_stud2 = {y: 70}

    j = "Java_ooprogramming"
    k = "Python_Scripting"

    stud1_det = {"lnumb": x, j: 40, k: 69}
    stud2_det = {"lnumb": y, j: 70, k: 58}
    module1 = {"name": j, "stud1": 40, "stud2": 70}
    module2 = {"name": k, "stud1": 69, "stud2": 58}
    # Dictionary for L number, Java and python grades for both students

    #python_stud1 = {x: 69}
    #python_stud2 = {y: 58}
    # Dictionary for L number and python grade for both students

    #print(module1["stud1"])
    #Check for the module mark value

    #stud1 = {java_stud1,python_stud1[x]}

    print("")


    print("Student 1 details are as follows : ")
    #print(stud1)
    print ("The L-number of the Student 1 is "+x)
    print("The grade of the module, "+ j +" is : "+format(stud1_det[j]))
    print("The grade of the module, " + k + " is : " + format(stud1_det[k]))
    # returns Student 1 grades

    #print(student1_details)

    # Printing grade details of Student 1

    print("")

    # Printing grade details of Student 2

    print("Student 2 Details are as follows : ")
    #print(java_stud2[1])
    #print(python_stud2)
    # print(stud2)
    print("The L-number of the Student 2 is " + y)
    print("The grade of the module, " + j + " is : " + format(stud2_det[j]))
    print("The grade of the module, " + k + " is : " + format(stud2_det[k]))

    # returns Student 2 grades

    #print(student2_details)

    print("\n")
print("Thank you for using my application")

# End of the code