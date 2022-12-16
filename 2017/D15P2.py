# Real input
val_a = 699
val_b = 124

# Test input
# val_a = 65
# val_b = 8921

factor_a = 16807
factor_b = 48271
num_iters = 5*(10**6)
score = 0

def gen(x, factor, bitshift):
  retval = ((x*factor) % 2147483647)
  while retval&((1<<bitshift)-1):
    retval = ((retval*factor) % 2147483647)
  return retval

for i in range(num_iters):
  if i%10**5 == 0:
    print(i)
  val_a = gen(val_a, factor_a, 2)
  val_b = gen(val_b, factor_b, 3)
  score += (val_a^val_b)&((1<<16)-1) == 0
