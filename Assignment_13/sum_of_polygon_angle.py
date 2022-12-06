print("demonstrate sum of polygon angle")
def polygon(value1):
    ans = (value1-2)*180
    return ans

def main():
    print("Enter the n side: ")
    side1 = int(input())

    sum = polygon(side1)
    print("sum of Polygon angle is: ",sum)
if __name__=="__main__":
    main()

# print("sum of polygon is: ")
# polygon = int(input())
# ans = (polygon-2)*180
# print("sum of loygon is: ",ans)