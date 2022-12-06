def checkyear(year):

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():

    year = int(input("Enter a year : "))
    if (checkyear(year)):
        print("Leap Year")
    else:
        print("Not a Leap Year")


if __name__=="__main__":
    main()