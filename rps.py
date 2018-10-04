#rock,paper,scissor
import random
a=['r','p','s']
s1=0
s2=0
while(True):
	b=input("enter rock,paper or scissor")
	c=random.choice(a)
	print("you chose ",b,"computer chose ")
	if(b!='p' and b!='r' and b!='s'):
		print("wrong input")
		if(c==b):
			print("its a tie")
		elif((c=='r' and b=='p') or (c=='p' and b=='s') or (c=='s' and b=='r')):
			s1=s1+1
			print("you win",s1,"times")
		else:
			s2=s2+1
			print("computer wins ",s2," times")
			break
	if(s1==3):
		print("computer wins finally")
	else:
		print("you win finally")

