# Demonstrate the find amount of potato

def count(value):
    formula = value.count("potato")
    return formula

def main():
    print("Enter The Vegetables:")
    num = input()

    total = count(num)
    print("Ans is: ",total)

if __name__=="__main__":
    main()