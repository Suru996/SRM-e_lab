a = int(input())
b = int(input())
c = []
for x in range(a,b+1):
  sum = 0
  d = x
  e = len(str(x))
  while(d > 0):
    r = d % 10
    sum += r ** e
    d = int(d / 10)
  if (sum == x):
    print(x)
