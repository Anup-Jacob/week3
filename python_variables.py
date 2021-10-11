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

    j = "Java_ooprogramming"
    k = "Python_Scripting"

    #stud1_det = {"lnumb": x, j: 40, k: 69}
    #stud2_det = {"lnumb": y, j: 70, k: 58}
    module1 = {"name": j, x: 40, y: 70}
    module2 = {"name": k, x: 69, y: 58}
    # Dictionary for L number, Java and python grades for both students


    print("")


    print("Student 1 details are as follows : ")
    #print(stud1)
    print ("The L-number of the Student 1 is "+x)
    print("The grade of the module, "+ j +" is : "+format(module1[x]))
    print("The grade of the module, " + k + " is : " + format(module2[x]))
    # returns Student 1 grades

    print("")

    # Printing grade details of Student 2

    print("Student 2 Details are as follows : ")
    #print(java_stud2[1])
    #print(python_stud2)
    # print(stud2)
    print("The L-number of the Student 2 is " + y)
    print("The grade of the module, " + j + " is : " + format(module1[y]))
    print("The grade of the module, " + k + " is : " + format(module2[y]))

    # returns Student 2 grades

    #print(student2_details)

    print("\n")
print("Thank you for using my application")

# End of the code