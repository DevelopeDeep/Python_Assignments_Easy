# Demonstrate the evaluate the equations

def eq(value):
    formula = eval(value)
    return formula
def main():
    print("enter the eq:")
    num = input()

    total = eq(num)
    print("The ans is: ",total)

if __name__=="__main__":
    main()