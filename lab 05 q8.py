print("Muhammad Huzaifa")
print("18B-048-CS-A")
print("LAB 05 PROGRAMMING EXERCISE")
print("Question 8")

def reverse_name():
    name= str(input('Enter Your Name Please: '))
    casefolded= name.casefold()
    reverse= casefolded[::-1]
    print('Your name in reverse is: ',reverse)
    
