from llist import dllist, dllistnode
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

class Data:
  blocks: dllist
  
  def __init__(self):
    self.blocks = dllist()
  
  def __str__(self):
    return "".join([str(block.value) for block in self.blocks.iternodes()])
  
  def append(self, size: int, file_id: int):
    self.blocks.append(Block(size, file_id))
  
  def split(self, free_block: dllistnode, size: tuple[int, int]):
    x, y = size
    assert(x+y == free_block.value.size)
    free_block.value.size = x
    new_block = Block(y, -1)
    self.blocks.insertafter(new_block, free_block)
  
  def move(self, file_block: dllistnode, free_block: dllistnode):
    assert(file_block.value.size == free_block.value.size)
    free_block.value.file_id = file_block.value.file_id
    file_block.value.file_id = -1
    if file_block.next != None:
      after: Block = file_block.next.value
      if after.file_id == -1:
        file_block.value.size += after.size
        self.blocks.remove(file_block.next)
    if file_block.prev != None:
      before: Block = file_block.prev.value
      if before.file_id == -1:
        file_block.value.size += before.size
        self.blocks.remove(file_block.prev)
  
  def split_and_move(self, file_block: dllistnode, free_block: dllistnode):
    assert(file_block.value.size <= free_block.value.size)
    if file_block.value.size != free_block.value.size:
      self.split(free_block, (file_block.value.size, free_block.value.size - file_block.value.size))
    self.move(file_block, free_block)
    
  def find_free_block(self, file_block: dllistnode) -> dllistnode:
    right = file_block
    left = self.blocks.first
    while right != left:
      if left.value.file_id == -1 and left.value.size >= right.value.size:
        return left
      left = left.next
    return None
  
  def checksum(self) -> int:
    total = 0
    pos = 0
    for node in self.blocks.iternodes():
      block = node.value
      for _ in range(block.size):
        if block.file_id != -1:
          total += (pos*block.file_id)
        pos += 1
    return total

def read() -> Data:
  data: Data = Data()
  is_file = True
  file_id = 0
  for char in content.strip():
    size = int(char)
    if is_file:
      data.append(size, file_id)
      file_id += 1
    else:
      data.append(size, -1)
    is_file = not is_file
  return data

data = read()
#print(data)

right = data.blocks.last
while right:
  if right.value.file_id == -1:
    right = right.prev
    continue
  free = data.find_free_block(right)
  if free:
    data.split_and_move(right, free)
    #print(data)
  right = right.prev
  
print(data.checksum())
