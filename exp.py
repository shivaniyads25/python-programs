try:
	a=int(input("Enter a:"))
	b=int(input("Enter b:"))
	c=a+b
	d=a-b
	e=a*b
	f=a/b
	print("sum= ",c)
	print("difference=",d)
	print("multiplication=",e)
	print("division=",f)
except Exception:
	print("cannot divide number by 0")
else:
	print("calculation succesfully done")   
