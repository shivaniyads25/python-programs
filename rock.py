import random
options=["rock","paper","scissor"]
player=raw_input("rock, paper or scissor?")
print "player got",player
comp=random.choice(options)
print "comp got",comp
if player==comp:
	print("draw")
elif player=="rock" and comp=="paper":
	print("comp wins")
elif player=="paper" and comp=="scissor":
	print("comp wins")
elif player=="scissor" and comp=="rock":
	print("comp wins")
elif player=="paper" and comp=="rock":
	print("player wins")
elif player=="scissor" and comp=="paper":
	print("player wins")
elif player=="rock" and comp=="scissor":
	print("player wins")