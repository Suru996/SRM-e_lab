a = int(input())
b = []
sum = 0
for x in range(0,a):
  d = int(input())
  b.append(d)
for x in range(0,a):
  if(b[x]%2 != 0 and b[x] > 0):
    sum += b[x]
 print("Sum of positive odd numbers:",sum)
