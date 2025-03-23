from bitarray import bitarray

def f(x):
  rev = ~x
  rev.reverse() # in place, so can't do this inline
  return x + [0] + rev

def chk(x):
  if len(x) % 2 == 1:
    return x
  even_bits = x[0:len(x):2]
  odd_bits = x[1:len(x):2]
  return chk(~(even_bits ^ odd_bits))

def fill(size, seed):
  bits = bitarray(seed)
  while len(bits) < size:
    bits = f(bits)
  bits = bits[:size]
  print(f"Used {bits.nbytes} bytes during computation")
  return chk(bits)

print(fill(272, "11011110011011101"))
print(fill(35651584, "11011110011011101"))
