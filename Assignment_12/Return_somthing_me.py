# Demonstrate return somthing to me

def number(a):
    formula = ('"something' + " " + a)
    return formula
def main():
    print("Enter input")
    num = input()

    total = number(num)
    print("give me somthing",total)

if __name__=="__main__":
    main()