# LCM : Least common multiple/ Lowest common multiple
# It is the smallest positive integer that is divisible by both "a" and "b"
def main():

    a = int(input("Enter num1 : "))
    b = int(input("Enter num2 : "))

    # Lets find bigger number
    if a > b:
        bigger = a
    else:
        bigger = b

    while(True):
        if bigger % a == 0 and bigger % b == 0:
            lcm = bigger
            break
        bigger += 1

    print("The LCM of {} and {} is : {}".format(a, b, lcm))

if __name__=="__main__":
    main()