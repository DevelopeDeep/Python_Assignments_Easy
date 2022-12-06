# Demonstrate the how many D are there

def eq(value):
    formula = value.lower().count('d')
    return formula
def main():
    print("Enter the sentence")
    num = input()

    total = eq(num)
    print("Total Count is:",total)

if __name__=="__main__":
    main()