print("Demonstration of boolean to string conversion")

def Bool(value):
	ans = str(bool(value <=0))
	return ans
def main():
	print("Enter the value: ")
	no = int(input())
	sum = Bool(no)
	print("Boolean to sting: ",sum)
	print(type(sum))
if __name__==("__main__"):
	main()
