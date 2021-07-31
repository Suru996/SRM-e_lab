a = int(input())
b = {}
for x in range(1,a+1):
  b.update({x:x ** 2})
print(b)
