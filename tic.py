
#tic-tac-toe game
#giving values to list
a=["1","2","3","4","5","6","7","8","9"]
#defining fuction
def  ttt_board():
	print(a[0],"|",a[1],"|",a[2],"|")
	print("-----------")
	print(a[3],"|",a[4],"|",a[5],"|")
	print("-----------")
	print(a[6],"|",a[7],"|",a[8],"|")
	return

player1=True
#entering into loop
while True:
	ttt_board()
	s=input("choose your place on board:")
	#giving conditions
	if(s in a):
		if(a[int(s)-1]=='X' or a[int(s)-1]=='O'):
			print("This place has been occupied by other player.Please choose another place.")
			continue
		else:
			if(player1):
				print("PLAYER 1>>")
				a[int(s)-1]='X'
				player1=not player1
			else:
				print("PLAYER 2>>")
				a[int(s)-1]='O'
				player1=not player1
	#giving condition for rows

			for i in(0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
					print("Game over")
					if(a[i]=='X'):
						print("Hurrah!! Player 1 won the game!!")
					else:
						print("Hurrah!! Player 2 won the game!!")
					ttt_board()
					exit()
					#giving condition for columns
			for i in range(3):
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					print("Game over")
					if(a[i]=='X'):
						print("Hurrah!! Player 1 won the game!!")
					else:
						print("Hurrah!! Player 2 won the game!!")
					ttt_board()
					exit()
			#giving condition for diagonals
			if(a[0]==a[4] and a[0]==a[8]):
				print("Game over")
				if(a[4]=='X'):
					print("Hurrah!! Player 1 won the game!!")
				else:
					print("Hurrah!! Player 2 won the game!!")
				ttt_board()
				exit()
			#giving condition for diagonals
			if(a[2]==a[4] and a[2]==a[6]):
				print("Game over")
				if(a[4]=='X'):
					print("Hurrah!! Player 1 won the game!!")
				else:
					print("Hurrah!! Player 2 won the game!!")
				ttt_board()
				exit()

