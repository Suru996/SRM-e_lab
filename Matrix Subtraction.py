m = int(input())
n = int(input())
d = []
f = []
for x in range(0,m):
  c = []
  for x in range(0,n):
    e = int(input())
    c.append(e)
  d.append(c)
for x in range(0,m):
  c = []
  for x in range(0,n):
    e = int(input())
    c.append(e)
  f.append(c)
print("Matrix 1")
for x in range(0,m):
  for x in range(0,n):
    print(d[x][y],end =' ')
  print()
print("Matrix 2")
for x in range(0,m):
  for x in range(0,n):
    print(f[x][y],end = ' ')
  print()
print("Difference of Matrix")
for x in range(0,m):
  for x in range(0,n):
    sum = d[x][y]  f[x][y]
    print(sum, end = ' ')
  print()
