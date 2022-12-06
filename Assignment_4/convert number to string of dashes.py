# Demonstrate the convert number to string of dashes

def number(value):
    formula = value * "-"
    return formula

def main():

    print("enter value:")
    num = int(input())

    total = number(num)
    print("num to dashes:",total)

if __name__=="__main__":
    main()

