
def main():
	test_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}

	# printing original dictionary
	print("The original dictionary is : "+ str(test_dict))

	# Convert key-values list to flat dictionary
	# using dict() + zip()
	res = dict(zip(test_dict['month'], test_dict['name']))

	# printing result
	print("Flatend dictionary : " + str(res))

if __name__=="__main__":
	main()
