import random
a=['r','p','s']
a1=0
a2=0
while(True):
	b=input("enter rock,paper or scissor")
	c=random.choice(a)
	print("you chose ",b,"computer chose ")
	if(b!='p' and b!='r' and b!='s'):
		print("wrong input")
		if(c==b):
			print("its a tie")
		elif((c=='r' and b=='p') or (c=='p' and b=='s') or (c=='s' and b=='r')):
			a1=a1+1
			print("you win",s1,"times")
		else:
			a2=a2+1
			print("computer wins ",a2," times")
			break
	if(a1==3):
		print("computer wins finally")
	else:
		print("you win finally")
