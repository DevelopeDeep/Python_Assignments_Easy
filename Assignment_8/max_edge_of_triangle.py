print("Demonstration maximum edge of a triangle")
def triangle(value1, value2,):
    ans = value1+value2-1
    return ans

def main():
    print("Enter value of edge1 :")
    side1 = int(input())
    print("Enter value of edge2 :")
    side2 = int(input())

    sum = triangle(side1,side2)

    print("maximum edge of tringle is: ",sum)
if __name__=="__main__":
    main()