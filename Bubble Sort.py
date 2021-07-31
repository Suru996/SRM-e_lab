a = int(input())
c = []
temp = 0
for x in range(0,a):
  b = int(input())
  c.append(b)
for x in range(0,a-1):
  for y in range(0,a-1):
    if(c[y] > c[y + 1]):
      temp = c[y + 1]
      c[y + 1] = c[y]
      c[y] = temp
  if(x == 2):
      print(*c)
print("Sorted array:")
print(*c)
