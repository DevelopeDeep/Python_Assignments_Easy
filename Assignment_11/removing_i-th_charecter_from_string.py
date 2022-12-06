
def remove(str, i):
	
	for j in range(len(str)):
		if j == i:
			str = str.replace(str[i], "", 1)
	return str

str = input("Enter the string : ")
i = int(input("Enter the index : "))

# print the new string

print("The new string : ", remove(str, i))
