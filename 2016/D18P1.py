myfile = open("input2.txt")
content = myfile.read()[:-1]

content = "." + content + "."

def generate_tile(three_tiles):
  if ((three_tiles == "^..")
    or (three_tiles == "..^")
    or (three_tiles == "^^.")
    or (three_tiles == ".^^")):
    return "^"
  else:
    return "."

def generate_row(row):
  new_row = []
  for i in range(len(row)-2):
    new_row.append(generate_tile(row[i:i+3]))
  return "".join(new_row)

rows = [content]
for i in range(39):
  rows.append("." + generate_row(rows[-1]) + ".")
  print(rows[-1])

print("".join(rows).count(".")-(2*len(rows)))
