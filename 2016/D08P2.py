content = open("input.txt").read()

import numpy as np
screen = np.zeros((6,50))
#screen = np.zeros((3,7))

for line in content.splitlines():
  line = line.split()
  match line[0]:
    case "rect":
      num1, num2 = list(map(int, line[1].split('x')))
      screen[:num2, :num1] = 1
    case "rotate":
      match line[1]:
        case "column":
          column_num = int(line[2].split('=')[1])
          screen[:,column_num] = np.roll(screen[:,column_num],int(line[-1]))
        case "row":
          row_num = int(line[2].split('=')[1])
          screen[row_num, :] = np.roll(screen[row_num, :],int(line[-1]))
        case _:
          assert(False)
    case _:
      assert(False)
  print(screen)

print(screen.sum())

screen_str = ""
for row in screen.tolist():
  screen_str += "".join(["#" if x == 1.0 else "." for x in row])
  screen_str += "\n"

print(screen_str)
