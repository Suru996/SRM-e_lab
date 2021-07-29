m = int(input())
n = int(input())
c = []
for x in range(0,m):
  a = []
  for y in range(0,n):
    b = int(input())
    a.append(b)
  c.append(a)
for x in range(0,m):
  for y in range(0,n):
    if(x == y):
      print(c[x][x])
