def fib(num):
  sequence = [1,2]
  if num < 2:
    return sequence
  else:
    i = 0
    while i < num:
      sequence.append(sequence[-1] + sequence[-2])
      i += 1
    return sequence

