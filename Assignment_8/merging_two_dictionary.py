def main():
	a = { 'x' : 31, 'y' : 23}
	b = { 'y' : 33, 'z' : 43}
	c = a.copy()
	c.update(b)
	print("dict a : ", a)
	print("dict b : ", b)
	print("updated dictionary : {}".format(c))

if __name__=="__main__":
	main()
