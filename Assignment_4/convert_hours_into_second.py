
print("Demonstration of convert hours into second")

def hours(Value1):
    Ans = 3600*Value1
    return Ans

def main():

    print("Enter the Value in hours: ")
    num1 = int(input())

    sec = hours(num1)
    print("Hours into second is:",sec)
if __name__=="__main__":
    main()