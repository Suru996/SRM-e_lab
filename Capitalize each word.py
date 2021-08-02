na = input()
a = open(na,'w+')
b = int(input())
d = []
for x in range(0,b):
  c = input()
  d.append(c)
for x in range(0,b):
  a.writelines('%s\n'%d[x].title())
a = open(na)
for x in range(0,b):
  print(a.realine())
a.close()
