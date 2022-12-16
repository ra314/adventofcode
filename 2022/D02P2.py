myfile = open("input2.txt")
content = myfile.read()

def convert_to_RPS(char):
  match char:
    case "A":
      return "ROCK"
    case "B":
      return "PAPER"
    case "C":
      return "SCISSOR"
    case "X":
      return "ROCK"
    case "Y":
      return "PAPER"
    case "Z":
      return "SCISSOR"
  assert(False)

def score(p1, p2):
  score = 0
  match p2:
    case "ROCK":
      score = 1
    case "PAPER":
      score = 2
    case "SCISSOR":
      score = 3
  match p1:
    case "ROCK":
      match p2:
        case "ROCK":
          return 3+score
        case "PAPER":
          return 6+score
        case "SCISSOR":
          return 0+score
    case "PAPER":
      match p2:
        case "ROCK":
          return 0+score
        case "PAPER":
          return 3+score
        case "SCISSOR":
          return 6+score
    case "SCISSOR":
      match p2:
        case "ROCK":
          return 6+score
        case "PAPER":
          return 0+score
        case "SCISSOR":
          return 3+score

total = 0
for line in content.splitlines():
  line = line.split()
  p1 = line[0]
  p2 = line[1]
  match p2:
    # Lose
    case "X":
      p2 = chr(((ord(p1)-ord("A")-1)%3)+ord("A"))
    # Draw
    case "Y":
      p2 = p1
    # WIN
    case "Z":
      p2 = chr(((ord(p1)-ord("A")+1)%3)+ord("A"))
  p1 = convert_to_RPS(line[0])
  p2 = convert_to_RPS(p2)
  total += score(p1, p2)

print(total)




#### POST HOC CLEN
total = 0
for line in content.splitlines():
  line = line.split()
  # Convert ABC to 012
  p1 = ord(line[0]) - ord("A")
  # Convert from xyz to 012
  p2 = ord(line[1]) - ord("X")
  score = p2 * 3
  # Shift downwards by 1
  # Now lose, draw, win are -1, 0, 1
  p2 -= 1
  # Rotate in the desired direction to find the right choice
  p2 = (p1 + p2) % 3
  # Scoring for your hand. ie 123 for rock paper scissor
  score += p2 + 1
  total += score

print(total)

### ONELINER
sum([((ord(line[2])-ord("X")) * 3) + ((((ord(line[2])-ord("X"))-1)+(ord(line[0]) - ord("A")))%3) + 1 for line in content.splitlines()])
