def bubble_sort(a,n):
  for x in range(0,n-1):
    for y in range(0,n-1):
      if(a[y]>a[y+1]):
        temp = a[y+1]
        a[y+1] = a[y]
        a[y] = temp
  return a

n = int(input())
a = []
for x in range(0,n):
  b = int(input())
  a.append(b)
a = bubble_sort(a,n)
print("Sequence of integers:",a[0]-1,"to",a[n-1]+1)
