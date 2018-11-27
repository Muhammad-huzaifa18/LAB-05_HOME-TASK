print("Muhammad Huzaifa")
print("18B-048-CS-A")
print("LAB 05 PROGRAMMING EXERCISE")
print("Question 1")
def area():
    import math
    print('Area of the cylinder')
    r_1 = eval(input('Enter the radius of the cylinder: '))
    h_1 = eval(input('Enter the height of the cylinder: '))
    a_1 = (2* math.pi * r_1 * h_1) + (2* math.pi * r_1**2)
    print("The area of the cylinder is {0:.{1}f}cm\u00b2".format(a_1, 4))
area()
def volume():
    import math
    print('Volume of the cylinder')
    r_2= eval(input('Enter the radius of the cylinder: '))
    h_2 = eval(input('Enter the radius of the cylinder: '))
    v_1 = (math.pi * (r_2**2) * h_2)
    print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(v_1, 4))
volume()
