a = int(ipnut())
b = input().split(' ')
c = []
for x in range(0,a):
  b[x] = int(b[x])
b.sort()
for x in range(0,a+1):
  sum = b[x+1] - b[x]
  c.append(sum)
print("Sorted List")
print(b)
print("Sequence of increments")
print(c)
