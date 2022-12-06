# max and min number in list

def number(num1, num2, num3, num4, num5, num6):
    formula = [num1,num2,num3,num4,num5,num6]
    return formula

def main():
    print("enter value1")
    num1 = int(input())
    print("enter value1")
    num2 = int(input())
    print("enter value1")
    num3 = int(input())
    print("enter value1")
    num4 = int(input())
    print("enter value1")
    num5 = int(input())
    print("enter value1")
    num6 = int(input())

    total = number(num1, num2, num3, num4, num5, num6)
    print(list,[num1, num2, num3, num4, num5, num6])
    print("Max Number is list in:",max(total))
    print("Min number is list in:",min(total))
    print("Addition of list is:",sum(total))

if __name__=="__main__":
    main()



