# Demonstrate the buggy code 4
def greeting(a):
    formula = (a+'!"')
    return formula
def main():
    print("Whats your name ")
    num = input()

    total = greeting(num)
    print('"Hello,',total)

if __name__=="__main__":
    main()


