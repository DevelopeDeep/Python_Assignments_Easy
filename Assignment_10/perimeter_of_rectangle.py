# Demonstrate the find the perimeter of a rectangle

def number(a,b):
    formula = a*2+b*2
    return formula

def main():
    print("Enter value1: ")
    num1 = int(input())
    print("Enter value2: ")
    num2 = int(input())

    total = number(num1,num2)
    print("ans is: ",total)

if __name__=="__main__":
    main()

