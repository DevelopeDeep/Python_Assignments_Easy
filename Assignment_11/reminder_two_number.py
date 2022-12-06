print("Demonstrate the reminder of tow number")
def reminder(value1, value2):
    ans = value1%value2
    return ans

def main():
    print("Enter the first value: ")
    no1 =int(input())
    print("Enter the second value: ")
    no2 =int(input())

    sum = reminder(no1, no2)
    print("The reminder is: ",sum)
if __name__=="__main__":
    main()