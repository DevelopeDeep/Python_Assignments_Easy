print("Demonstrate the string to integer")
def number(value1):
    formula = int(value1)
    return formula
def main():
    print("enter the value: ")
    num = (input())

    total = number(num)

    print("Your ans is:",total)
    print(type(total))

if __name__=="__main__":
    main()