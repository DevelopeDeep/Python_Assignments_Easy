def main():
    x = int(input("Num1 : "))
    y = int(input("Num2 : "))
    print("Before swaping x = {}, y = {}".format(x, y))

    # swaping
    y, x = x, y
    print("After swaping x = {}, y = {}".format(x,y))

if __name__ =="__main__":
    main()
