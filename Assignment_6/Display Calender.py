def main():
    import calendar

    y = int(input("Enter Year : "))
    m = int(input("Enter Month : "))

    try:
        print("Calender")
        print(calendar.month(y, m))
    except:
        print("Out of range")

if __name__=="__main__":
    main()
