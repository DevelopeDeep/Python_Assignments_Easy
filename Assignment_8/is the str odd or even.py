# Demonstrate is the str odd or even

def number(a):
    formula = len(a)%2==0
    return formula

def main():
    print("Enter value: ")
    num = input()

    total = number(num)
    print("Ans is: ",total)

if __name__=="__main__":
    main()