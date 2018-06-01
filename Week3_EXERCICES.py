
def read_number():
	#think to hide echo when using raw_input()!!!
	nbr = int(raw_input('Enter number from 1 to 3: '))
	while nbr not in [1,2,3] :
		print 'Please try again'
		nbr = int(raw_input('Enter number from 1 to 3: '))
	return nbr

def battle(player1, player2):
	"""return score result"""
	if player1==player2 :
		return (0,0)
	elif player1 < player2:
		return (1,0)
	else : 
		return (0,1)
		
def score_notify(score1, score2):
	"""return message notification according to winner"""
	if score1 > score2 :
		result = "Player A won"
	elif score1 < score2 : 
		result = "Player B won"
	else :
		result = "Tied Score"
	return result

def main_game():
	game_scoreA=0
	game_scoreB=0
	round = 0
	while (True) :
		#start a round
		round+=1
		print '------------------------'
		print 'Round',round,'is started'
		print '------------------------'
		print 'Player A :'
		player1= read_number()
		print 'Player B :'
		player2= read_number()
		
		#round result
		round_scoreA,round_scoreB = battle(player1,player2)
		print "->For this round", score_notify(round_scoreA, round_scoreB)
		
		#Update game scores and display it
		game_scoreA=game_scoreA+round_scoreA
		game_scoreB=game_scoreB+round_scoreB	
				
		print score_notify(game_scoreA, game_scoreB),': ', str(game_scoreA), 'VS', str(game_scoreB)
		
		#more Game?
		newgame=raw_input('Play again? (y/n) : ')
		while newgame not in ['y','Y','N','n']:
			newgame=raw_input('(y/n)? : ')
		if newgame in ['n','N']:
			break;
	print "You have played", round, "Rounds"
	print "Nice to meet you in another game, Bye!"

#for debugging only
#read_number()
#print battle (2,2), battle (1,3), battle (3,2)

main_game()