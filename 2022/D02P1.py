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
  p1 = convert_to_RPS(line[0])
  p2 = convert_to_RPS(line[1])
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
  # Initially the score is just your hand. eg: 2 for paper
  score = p2 + 1
  # Let suppose your hand is scissor and your opponent is rock.
  # We need to shift the reepresentation so that your hand = 1 (the middle)
  p1 = (p1 - (p2 - 1)) % 3
  # Now p1 is 0, 1 or 2 which correspond to win, draw and loss
  # Because in RPS. P beats what's to it's left and loses to what's to it's right
  # Let's invert that
  p1 = 2 - p1
  score += p1 * 3
  total += score

print(total)
