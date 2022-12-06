
def wordsBiggerThanLengthK(k,str):
	txt = str.split()
	listOfWords = []
	for i in txt:
		if len(i) > k:
			listOfWords.append(i)
	return listOfWords

str = input("Enter the string : ")
k = int(input("Enter the length K : "))

listword = wordsBiggerThanLengthK(k, str)

print("\nThe original string ' {} '".format(str))

print("Words which are greater than length {} ".format(k))
print(listword)
