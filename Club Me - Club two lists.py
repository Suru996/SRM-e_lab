a = int(input())
d = []
e = []
for x in range(0,a):
  c = int(input())
  d.append(c)
b = int(input())
for x in range(0,b):
  c = int(input())
  e.append(c)
for x in range(0,b):
  d.append(e[x])
d.sort()
print("Sorted list is:",d)
