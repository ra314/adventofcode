myfile = open("input.txt")
content = myfile.read()

dancers = list("abcdefghijklmnop")
dancers = list("abcde")
start_index = 0

def get_new_index(index):
  return (start_index + index) % len(dancers)

for line in content[:-1].split(','):
  if line[0] == 's':
    start_index += (int(line[1:]))
    start_index = (start_index % len(dancers))
  if line[0] == 'x':
    num1 = int(line[1:].split('/')[0])
    num2 = int(line[1:].split('/')[1])
    num1 = get_new_index(num1)
    num2 = get_new_index(num2)
    dancer1 = dancers[num1]
    dancers[num1] = dancers[num2]
    dancers[num2] = dancer1
  if line[0] == 'p':
    char1 = (line[1:].split('/')[0])
    char2 = (line[1:].split('/')[1])
    num1 = dancers.index(char1)
    num2 = dancers.index(char2)
    dancers[num1] = char2
    dancers[num2] = char1

print("".join(dancers))
