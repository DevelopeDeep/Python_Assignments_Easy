def main():

	str = "this is a string"
	str = str.split(" ") # str is converted to a list of string.
	print(" Splitting a string : ", str)

	str2 = " ".join(str) # you can insert "_" in
	print("Joining a string : ", str2)

if __name__=="__main__":
	main()
