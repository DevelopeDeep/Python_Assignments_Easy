# HCF : Highest common factor
# is the largest positive integer that evenly divides the number without a reminder

def main():
    a = int(input("Enter num1 : "))
    b = int(input("Enter num2 : "))

# Lets find biggest number
    if a < b:
        smaller = a
    else:
        smaller = b
    hcf = 0
    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            hcf = i
    print("The hcf of {} and {} is : {}".format(a, b, hcf))

if __name__=="__main__":
    main()
