# BMI = weight / height
def main():

    h = float(input("Enter your height in feet : "))
    w = float(input("Enter your weight in kilo : "))

    bmi = w/(h**2)

    print("The BMI is = ", bmi)

if __name__=="__main__":
    main()
