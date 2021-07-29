a = int(input())
d = []
for x in range(0,a):
  c = []
  for y in range(0,b):
    if(x == y):
      c.append(1)
    else:
      c.append(0)
  d.append(c)
for x in range(0,a):
  for x in range(0,b):
    print(d[x][y])
