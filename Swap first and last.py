def swap(a,n):
  max = n-1
  min = 0
  temp = a[0]
  a[min] = a[max]
  a[max] = temp
  return a

n = int(input())
a = []
for x in range(0,n):
  c = int(input())
  a.append(c)
print("New list is:")
print(swap(a,n))
