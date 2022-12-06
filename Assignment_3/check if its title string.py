# Demonatrate the check if iots tile string

def title(value):
    formula = value.istitle()
    return formula

def main():
    print(" enter the value")
    num= input()

    total = title(num)
    print("Ans is :",total)

if __name__=="__main__":
    main()