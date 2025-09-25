def count_down(num):
    total=0
    while num>=0:
        print(num)
        total+=num
        num-=1
    return total
def count_up(num):
    total = 0
    while num<=0:
        print(num)
        total+=num
        num+=1
    return total
def main():
    number=int(input("Enter a number: "))
    resultdown=count_down(number)
    resultup=count_up(number)
    print("The sum of countdown number is:",resultdown)
    print("The sum of countup number is: ",resultup)
main()
