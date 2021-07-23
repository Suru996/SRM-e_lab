a = input()
b = len(a)
c = ''
for x in range(0,b):
  if(a[x] == ' '):
    c += '-'
  else:
    c += a[x]
print(c)
