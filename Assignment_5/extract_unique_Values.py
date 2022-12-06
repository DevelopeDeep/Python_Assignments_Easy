def main():
	test_dict = {'a' : [1, 62, 7, 8],
		'b' : [1, 11, 7, 5],
		'c' : [1, 11, 10, 8],
		'd' : [1, 2, 11, 8]}
	lstSet = set([ele for val in test_dict.values() for ele in val])
	print("unique value from dictionary values are : {} ".format(lstSet))
if __name__=="__main__":
	main()
