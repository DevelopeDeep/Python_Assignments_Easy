print("Demonstrate get first element in list")
def get_value(value1, value2, value3):
    ans = ([value1])
    return ans

def main():
    print("Enter number: ")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    first = (get_value(num1,num2,num3))

    print("Enter first value in list: ",first)
if __name__=="__main__":
    main()
