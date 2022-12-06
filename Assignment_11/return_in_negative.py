# Demonstrate the return negative

def number(a):
    formula = -a
    return formula
def main():
    print("enter number: ")
    num = int(input())

    total = number(num)
    print("Get return in Negativ Value: ",total)

if __name__=="__main__":
    main()
