a = input()
b = len(a)
c = ''
for x in range(0,b):
  if (a[x] == 'a' or a[x] == 'e' or a[x] == 'i' or a[x] == 'o' or a[x] == 'u'):
    continue
  else:
    c += a[x]
print(c)
