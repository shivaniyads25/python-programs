import random
p=0
while (p<=100):
	i=input("press r to roll the dice")
	if(i=='r'):
		r=random.randint(1,6)
		p=p+r
		print("you got ",r)
		print("new position is ",p)
	if(p==8):
		p=37
		print("you got a ladder")
	elif(p==11):
		p=2
		print("oops! you got a snake")
	elif(p==13):
		p=34
		print("you got a ladder")
	elif(p==25):
		p=4
		print("oops! you got a snake")
	elif(p==38):
		p=8
		print("oops! you got a snake")
	elif(p==40):
		p=68
		print("you got a ladder")
	elif(p==52):
		p=81
		print("you got a ladder")
	elif(p==65):
		p=46
		print("oops! you got a snake")
	elif(p==76):
		p=97
		print("you got a ladder")
	elif(p==89):
		p=70
		print("oops! you got a snake")
	elif(p==93):
		p=64
		print("oops! you got a snake")
	if(p==100):
		print("you won the game")
		exit()
	elif(p>100):
		print("stay in the game")
		p=p-r

