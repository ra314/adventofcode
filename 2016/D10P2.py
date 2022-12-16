myfile = open("input2.txt")
content = myfile.read()

from collections import defaultdict

output_chips = defaultdict(list)
bot_chips = defaultdict(list)
bot_instructions = {}
for line in content.splitlines():
  line = line.split()
  if line[0] == "value":
    bot_chips[int(line[-1])].append(int(line[1]))
  else:
    bot_instructions[int(line[1])] = line

def find_current_bot(bot_chips):
  for bot in bot_chips:
    if len(bot_chips[bot])==2:
      return bot
  return "NOT FOUND"

def execute_instruction(bot):
  bot_instruction = bot_instructions[bot]
  
  if (61 in bot_chips[bot]) and (17 in bot_chips[bot]):
    print(bot)
    print("This is the guy you're looking for")
  
  if bot_instruction[5] == "output":
    output_chips[int(bot_instruction[5+1])].append(min(bot_chips[bot]))
  else:
    bot_chips[int(bot_instruction[5+1])].append(min(bot_chips[bot]))
  if bot_instruction[10] == "output":
    output_chips[int(bot_instruction[10+1])].append(max(bot_chips[bot]))
  else:
    bot_chips[int(bot_instruction[10+1])].append(max(bot_chips[bot]))
  bot_chips[bot] = []

curr_bot = find_current_bot(bot_chips)
while curr_bot != "NOT FOUND":
  execute_instruction(curr_bot)
  curr_bot = find_current_bot(bot_chips)

print(output_chips[0][0]*output_chips[1][0]*output_chips[2][0])
