# Demonstrate the concatenating two integer list

def concatenate(l1=[1,2,3],l2=[4,5,6]):
    formula = (l1+l2)
    return formula

def main():
    print("list1:")
    num1 = input()
    print("list2:")
    num2 = input()

    total = concatenate(num1,num2)

    print("concatenation is:",[total])

if __name__=="__main__":
    main()

# Concatenating Two Integer Lists

# def function(value1, value2, value3, value4, value5, value6, value7, value8):
# 	formula = ([value1, value2] + [value3, value4, value5, value6, value7,value8])
# 	return formula
#
#
# def main():
# 	num1 = int(input("Enter first number: "))
# 	num2 = int(input("Enter second number: "))
# 	num3 = int(input("Enter third number: "))
# 	num4 = int(input("Enter forth number: "))
# 	num6 = int(input("Enter fifth number: "))
# 	num5 = int(input("Enter fifth number: "))
# 	num7 = int(input("Enter seventh number: "))
# 	num8 = int(input("Enter eighth number: "))
#
# 	total = function(num1, num2, num3, num4, num5, num6, num7, num8)
# 	print("Concatenate:",total)
#
# if __name__ == "__main__":
# 	main()


# l1 = [1,2,3]
# l2 = [4,5,6]
# print(l1+l2)
