myfile = open("input2.txt")
content = myfile.read()

import json

content = json.loads(content)

def parse_dict(dict_content):
  total = 0
  for value in dict_content.values():
    if value == "red":
      return 0
    elif type(value) == int:
      total += value
    elif type(value) == dict:
      total += parse_dict(value)
    elif type(value) == list:
      total += parse_list(value)
  return total

def parse_list(list_content):
  total = 0
  for value in list_content:
    if type(value) == int:
      total += value
    elif type(value) == dict:
      total += parse_dict(value)
    elif type(value) == list:
      total += parse_list(value)
  return total
    
print(parse_dict(content))
