import dataclasses

import reader
content = reader.read()


class Block:
  size: int
  file_id: int
  
  def __init__(self, size: int, file_id: int):
    self.size = size
    self.file_id = file_id
  
  def __str__(self):
    if self.file_id == -1:
      return "."*self.size
    return str(self.file_id)*self.size

def print_blocks(blocks: list[Block]):
  print("".join([str(block) for block in blocks]))

data: list[Block] = []
is_file = True
file_id = 0
for char in content.strip():
  size = int(char)
  if is_file:
    data.append(Block(size, file_id))
    file_id += 1
  else:
    data.append(Block(size, -1))
  is_file = not is_file

#print_blocks(data)

left_pointer = 1
right_pointer = len(data) - 1
while True:
  #print_blocks(data)
  
  if right_pointer <= left_pointer:
    break
  
  free_block: Block = data[left_pointer]
  file_block: Block = data[right_pointer]
  
  if free_block.file_id != -1:
    left_pointer += 1
    continue
  
  if file_block.file_id == -1:
    right_pointer -= 1
    continue
  
  print(left_pointer, right_pointer)
  
  if free_block.size > file_block.size:
    data.pop(right_pointer)
    data.insert(left_pointer, file_block)
    right_pointer -= 1
    free_block.size -= file_block.size
    left_pointer += 1
  elif free_block.size == file_block.size:
    data.pop(right_pointer)
    data[left_pointer] = file_block
    right_pointer -= 1
    left_pointer += 1
  else:
    free_block.file_id = file_block.file_id
    file_block.size -= free_block.size
    left_pointer += 1

#print_blocks(data)

def checksum(data: list[Block]) -> int:
  total = 0
  pos = 0
  for block in data:
    if block.file_id == -1:
      break
    for _ in range(block.size):
      total += (pos*block.file_id)
      pos += 1
  return total

print(checksum(data))
