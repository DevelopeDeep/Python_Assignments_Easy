def main():
    kilometers = float(input("Enter kilometers : "))
    conversionUnit = 0.621
    miless = kilometers * conversionUnit

    print("%0.3f kilometers is equal to %0.3f miles" % (kilometers, miless))

if __name__=="__main__":
    main()