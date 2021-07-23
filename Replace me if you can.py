a = input()
b = input()
c = len(a)
d = ''
for x in range(0,a):
  if(a[x] == b):
    d += '#'
  else:
    d += a[x]
print(d)
