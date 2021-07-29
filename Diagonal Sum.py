a = int(input())
b = int(input())
c = []
sum = 0
for x in range (0,a):
  d = []
  for y in range(0,b):
    e = int(input())
    d.append(e)
  c.append(d)
for x in range(0,a):
  sum += c[x][x]
print(sum)
