# Demonstrate the remove number from strings

def equation(value):
    formula= value = "".join(i for i in value if not i.isdigit())
    return value

def main():
    print("Enter the Value:")
    num = input()

    total = equation(num)
    print("Ans is:",total)

if __name__=="__main__":
    main()