n = int(input())
a = []
for x in range(0,a):
  b = int(input())
  a.append(b)
key = int(input())
for x in range(0,n):
  if(key == a[x]):
    print("Element is present at index",x)
    break
