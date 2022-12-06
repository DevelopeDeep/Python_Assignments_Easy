print("Demonstrate the name greeting!")

def greeting(value1):
    formula = ("Hello" + ' '+ value1 + '!')
    return formula
def main():
    print("Hi: ")
    num = input()

    total = greeting(num)
    print("Your name: ",total)

if __name__=="__main__":
    main()