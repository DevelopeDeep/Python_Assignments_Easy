# Demonstrate the Char-to-ASCII

def char(value):
    formula = ord(value)
    return formula

def main():
    print("Enter input:")
    num = input()
    print("Enter input:")
    num = int(input())
    total = char(num)
    print("Ans is:",total)

if __name__=="__main__":
    main()
