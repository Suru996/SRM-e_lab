a = int(input())
b = []
d = []
f = {}
for x in range(0,a):
  c = int(input())
  b.append(c)
e = int(input())
for x in range(0,e):
  c = int(input())
  d.append(c)
for x in range(0,a):
  f.update({b[x]:d[x]})
print(f)
