myfile = open("input.txt")
content = myfile.read()

x = 1
cycle = 1
values = []

def draw_crt(cycle, x):
  if x > 0:
    if abs(((cycle-1)%40)-(x%40)) <= 1:
      crt[cycle-1] = "#"

crt = list("." * (6*40))

for line in content.splitlines():
  match line.split()[0]:
    case "noop":
      draw_crt(cycle, x)
      cycle += 1
      
    case "addx":
      draw_crt(cycle, x)
      cycle += 1
      draw_crt(cycle, x)
      x += int(line.split()[-1])
      cycle += 1

  for i in range(6):
    print("".join(crt[40*i:40*(i+1)]))
  print()
