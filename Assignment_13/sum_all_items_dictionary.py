def main():
	test_dict = {'a' : 10,
				'b' : 11,
				'c' : 13,
				'd' : 65}

	sum = 0
	for i in test_dict.values():
		sum += sum + i
	print("Sum of all items is : {}".format(sum))

if __name__=="__main__":
	main()
