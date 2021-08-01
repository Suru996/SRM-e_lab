n = int(input())
m = int(input())
a = []
b = []
for x in range(0,n):
  c = int(input())
  a.append(c)
for x in range(0,m):
  c = int(input())
  b.append(c)
r = int(input())
for x in range(0,m):
  a.append(b[x])
print("The Extended List")
print(a)
print("The Reverse List")
a.reverse()
print(a)
a.remove(r)
print(a)
