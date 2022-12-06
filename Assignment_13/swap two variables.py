def main():
    a = int(input("Enter The value : "))
    b = int(input("Enter The value : "))

    print("Before swaping a = {}, b = {}".format(a, b))
    temp = a
    a = b
    b = temp

    print("After swaping a = {}, b = {}".format(a, b))

if __name__=="__main__":
    main()