# Real input
val_a = 699
val_b = 124

# Test input
# val_a = 65
# val_b = 8921

factor_a = 16807
factor_b = 48271
num_iters = 40*(10**6)
score = 0

def gen(x, factor):
  return ((x*factor) % 2147483647)

for i in range(num_iters):
  if i%10**6 == 0:
    print(i)
  val_a = gen(val_a, factor_a)
  val_b = gen(val_b, factor_b)
  val_anded = val_a^val_b
  val_truncated = val_anded&((1<<16)-1)
  score += val_truncated == 0
