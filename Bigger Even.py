a = int(input())
c = []
d = []
for x in range(0,a):
  b = int(input())
  c.append(b)
for x in range(0,a):
  if(c[x] % 2 == 0):
    d.append(c[x])
e = d[0]
for x in range(1,len(d)):
  if(d[x] > e):
    e =d[x]
print("Largest even number:",e)
