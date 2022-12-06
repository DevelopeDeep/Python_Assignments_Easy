# Demonstrate compare str by count characters

def numbers(a,b):
    formula = len(a)==len(b)
    return formula

def main():
    print("enter value1: ")
    num = input()
    print("enter value2: ")
    nu1 = input()

    total = numbers(num,nu1)
    print("compare is: ",total)

if __name__=="__main__":
    main()