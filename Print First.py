a = int(input())
c = [] 
e = []
for x in range(0,a):
  b = input()
  c.append(b)
for x in range(0,len(c)):
  s = set()
  d = []
  for y  in c[x]:
    if y not in s:
      d.append(y)
    s.add(y)
  e.append(d)
for x in range(0,len(e)):
  for y in range(0,len(e[x])):
    print(e[x][y],end= '')
print()
