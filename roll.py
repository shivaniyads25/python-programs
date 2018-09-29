import random

while True:
	i=input("enter 'r' to roll the dice")
	if(i=='q'):
		print("bye")
		exit()
	elif(i=='r'):
		print("you rolled a ",random.randint(1,6))
else:
	print(" ")