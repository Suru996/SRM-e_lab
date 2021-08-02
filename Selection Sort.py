def sel_sort(a,n):
  for x in range(0,n):
    mi = x
    for y in range(x+1,n):
      if(a[mi] > a[y]):
        mi = y
    temp = a[mi]
    a[mi] = a[x]
    a[x] = temp
    if(x == 2):
      print(*a)
  return a

n = int(input())
a = []
for x in range(0,n):
  b = int(input())
  a.append(b)
c = sel_sort(a,n):
  print("Sorted Array")
  print(*c)
