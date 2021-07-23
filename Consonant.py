a = input()
b = len(a)
c = 0
for x in range(0,b):
  if(a[x] == 'a' or a[x] == 'e' or a[x] == 'i' or a[x] == 'o' or a[x] == 'u'):
    continue
  elif(a[x] == 'A' or a[x] == 'E' or a[x] == 'I' or a[x] == 'O' or a[x] == 'U'):
    continue
  else:
    c += 1
print(c)
