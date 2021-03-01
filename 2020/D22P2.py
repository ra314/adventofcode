myfile = open("input.txt")
content = myfile.read()

###Parsing the input
import re
nums = [int(num) for num in re.findall("(\d+)\n", content)]
player1_cards = nums[:int(len(nums)/2)]
player2_cards = nums[int(len(nums)/2):]

###Playing the game
###The function returns a list
###The first element is a boolean which is True if player1 wins the game, false otherwise
###The second element is a list of the cards from the winning player
###The variable round_winner is true if player1 wins, false otherwise
game_num = 0
def play_game(player1_cards, player2_cards):
	global game_num
	game_num+=1
	local_game_num = game_num
	round_num = 0

	previous_card_configurations = []

	while min(len(player1_cards),len(player2_cards)) != 0:
		round_num += 1
		print(f"Game: {local_game_num}, Round: {round_num}")
		print(player1_cards)
		print(player2_cards)
		print()

		previous_card_configurations.append([player1_cards.copy(), player2_cards.copy()])
		if [player1_cards,player2_cards] in previous_card_configurations[:-1]:
			return [True, player1_cards]

		num1 = player1_cards.pop(0)
		num2 = player2_cards.pop(0)

		if len(player1_cards)>=num1 and len(player2_cards)>=num2:
			round_winner = play_game(player1_cards[:num1], player2_cards[:num2])[0]
		else:
			round_winner = num1>num2

		if round_winner:
			player1_cards.extend([num1, num2])
		else:
			player2_cards.extend([num2, num1])

	game_winner = len(player1_cards)!=0
	return [game_winner, player1_cards if game_winner else player2_cards]

###Calculating the score
sum = 0
cards = play_game(player1_cards,player2_cards)[1]
for i in range(len(cards),0,-1):
	sum += cards[len(cards)-i]*i

print(sum)