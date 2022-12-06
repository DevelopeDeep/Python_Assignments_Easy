def main():
# - quadratic quation ax^2+bx+c=0
# a, b, c = known numbers, where a !=0
# x = the unknown
# - descriminant = b**2 - (4* a* c)
# - x1 = (-b-sqrt(d))/2, x2 = (b-squrt(d))/2

# import complex math module
    import cmath

    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    c = int(input("Enter value of c : "))
# Calculating the discriminant
    dis = (b**2) - (4 * a*c)

# find two results
    x1 = (-b-cmath.sqrt(dis))/(2 * a)
    x2 = (-b + cmath.sqrt(dis))/(2 * a)

# printing the result
    print('The roots are')
    print(x1)
    print(x2)


if __name__=="__main__":
    main()