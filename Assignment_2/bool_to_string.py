# Demonstrate the bool into str

def number(flag):
    formula = str(flag)
    return formula

def main():
    print("Enter the value: ")
    num = input()

    total = number(num)
    print("Ans is: ",total)
    print(type(total))

if __name__=="__main__":
    main()
