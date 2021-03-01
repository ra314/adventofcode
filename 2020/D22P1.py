myfile = open("input.txt")
content = myfile.read()

###Parsing the input
import re
nums = [int(num) for num in re.findall("(\d+)\n", content)]
player1_cards = nums[:int(len(nums)/2)]
player2_cards = nums[int(len(nums)/2):]

###Playing the game
while min(len(player1_cards),len(player2_cards)) != 0:
	num1 = player1_cards.pop(0)
	num2 = player2_cards.pop(0)
	if num1>num2:
		player1_cards.extend(sorted([num1,num2], reverse = True))
	else:
		player2_cards.extend(sorted([num1,num2], reverse = True))

sum = 0
cards = player1_cards+player2_cards
for i in range(len(cards),0,-1):
	sum += cards[len(cards)-i]*i

print(sum)