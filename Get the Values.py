n = int(input())
d = []
e = []
f = {}
for x in range(0,n):
  a = int(input())
  d.append(a)
for x in range(0,n):
  a = int(input())
  e.append(a)
for x in range(0,n):
  f.update({d[x]:e[x]})
print("The dictionary is")
print(f)
k = int(input())
print(f[k])
