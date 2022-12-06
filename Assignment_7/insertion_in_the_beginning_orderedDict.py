
def main():
	from collections import OrderedDict
	
	# initialising orderd_dict
	iniordered_dict = OrderedDict([('Feb', '2'), ('Mar', '3')])

	# inserting items in starting of dict
	iniordered_dict.update({'Jan': '1'})
	iniordered_dict.move_to_end('Jan', last = False)

	# print result
	print("Ordered Dictionary after insertion : " + str(iniordered_dict))

if __name__=="__main__":
	main()
