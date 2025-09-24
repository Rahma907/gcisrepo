def rverse_string(s):
    for i in range(len(s)-1,-1,-1):
        print(s[i],end=" ")
def main():
    inpstr=input("Enter a string:  ")
    rverse_string(inpstr)
main()