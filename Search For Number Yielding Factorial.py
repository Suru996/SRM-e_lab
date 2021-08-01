n = int(input())
b = input().split(' ')
c = int(input())
f = 0
for x in range(0,n):
  b[x] = int(b[x])
for x in b:
  e = 1
  for y in range(1,x+1):
    e *= y
  if(e == c):
    f = x
    break
if(f > 0):
  print(f)
else:
  print("Not found")
  
