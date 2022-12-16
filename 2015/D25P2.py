CODE1 = 20151125
MULT = 252533
MOD = 33554393

# Finding the code index
target_row = 2947
target_col = 3029
#target_row = 3
#target_col = 4
target_col_cpy = target_col
target_code_index = 1

i = 2
while target_col != 1:
  target_col -= 1
  target_code_index += i
  i += 1

i = target_col_cpy
while target_row != 1:
  target_row -= 1
  target_code_index += i
  i += 1

curr_code = CODE1
code_index = 1
while code_index != target_code_index:
  curr_code *= MULT
  curr_code %= MOD
  code_index += 1
  if code_index % 1000000 == 0:
    print(code_index)

print(curr_code)
