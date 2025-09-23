'''
The question is to write a function to check if its even and odd 
and also finding the cube and square of the number
'''
def even_odd(x):#To find odd or even number
    if x%2==0:
        print("Even no.")
    else:
        print("Odd no:")
def square_cube(number):#To find square and cube of the number
    print("Square of the number is=" ,number**2)
    print("Cube of the number is=",number**3)
def main():#Calling the main function
    num=int (input("Enter your number:"))
    even_odd(num)
    square_cube(num)
main()
