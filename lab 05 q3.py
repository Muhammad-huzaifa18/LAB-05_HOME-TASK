print("Muhammad Huzaifa")
print("18B-048-CS-A")
print("LAB 05 PROGRAMMING EXERCISE")
print("Question 3")

def arithmetic_sequence():
    n = int(input("Please enter the number of the term you want to find: "))
    a= int(input("Please enter the first term: "))
    d= int(input("Please enter the common difference: "))
    an = a+((n-1)*d)
    print("The",str(n),"th term of the given sequence is: ",str(an))
    user=input("\nDo you want to find another term (Press 'yes' to continue, 'exit' to quit):")
    while user=='yes':
        arithmetic_sequence()
    else:
        print("Okay bye!,Thanks...!")
