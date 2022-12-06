def main():
    celsius = float(input("Celsius : "))
    fahrenheit = 9/5 * celsius + 32
    print("%0.2f celsius is equal to %0.2f fahrenheit" % (celsius, fahrenheit))

if __name__=="__main__":
    main()