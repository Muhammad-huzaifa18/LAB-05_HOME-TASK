print("Muhammad Huzaifa")
print("18B-048-CS-A")
print("LAB 05 PROGRAMMING EXERCISE")
print("Question 7")

def projectile(Vo,angle):
    import math
    degree = (angle*(math.pi/180))
    g = 9.8
    T = (2*Vo*math.sin(degree))/g
    print("The time of flight is" , T ,'(s)')
    H = ((Vo**2)*(math.sin(degree)**2)/(2*g))
    print("The height reached is" , H ,'(meters)')
    R = ((Vo**2)*(math.sin(degree*2))/g)
    print("The horizontal range is" , R ,'(meters)')
    
