n = int(input())
m = int(input())
d = []
for x in range(0,n):
  c = []
  for y in range(0,m):
    a = int(input())
    c.append(a)
  d.append(c)
print(d)
for x in range(0,n):
  for y in range(0,m):
    print(d[x][y],end = ' ')
  print()
