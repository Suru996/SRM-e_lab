a = input()
b = len(a)
uc = 0
lc = 0
sp = 0
for x in range(0,b):
  if(a[x].isupper()):
    uc += 1
  elif(a[x].islower()):
    lc += 1
  else:
    sp += 1
print(lc)
print(uc)
print(sp)
