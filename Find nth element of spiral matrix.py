n = int(input())
a = input().split(' ')
b = int(a[0])
c = int(a[1])
d = int(a[2])
e = input().split(' ')
f = []
i =0
for x in range(0,b):
  g = []
  for y in range(0,c):
    g.append(int(e[i]))
    i += 1
  f.append(g)
sr = 0
sc = 0
co = 0
while(sr < b and sc < c):
  for x in range(sc,b):
    co += 1
    if(co == d):
      print(f[sr][x])
  sr += 1
  for x in range(sr,c):
    co += 1
    if(co == d):
      print(f[x][c-1])
  c -= 1
  if(sr < b):
    for x in range(c-1,sc,-1):
      co += 1
      if(co == d):
        print(f[b-1][x])
    b -= 1
    if(sc < c):
      for x in range(b-1,sr,-1):
        co += 1
        if(co == d):
          printf(f[x][c-1])
      sc += 1
