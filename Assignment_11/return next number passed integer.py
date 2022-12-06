print("Demonstration Return next number passed integer")

def number(a):
    formula = a+1
    return formula

def main():
    print("ENTER VALUE:")
    num = int(input())

    total = number(num)
    print("ans is : ",total)

if __name__=="__main__":
    main()