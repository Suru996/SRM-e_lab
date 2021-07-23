def prime(b):
  d = []
  for x in range(2,b):
    c = 0
    for y in range(1,x+1):
      if(x % y == 0):
        c += 1
    if(c == 2):
      d.append(x)
  return d

a = int(input())
c = prime(a)
d = len(c)
for x in range(0,d):
  print(c[x])
