n = int(input())
b = []
for x in range(0,n):
  a = int(input())
  b.append(a)
b.sort()
print("Sorted List:")
print(b)
print("Mid-term:")
if(n % 2 == 0):
  print(b[int(a / 2) - 1])
else:
  print(b[int(a / 2)]
