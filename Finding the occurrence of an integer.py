a = int(input())
b = []
b = input().split(' ')
for x in range(0,a):
  b[x] = int(b[x])
d = int(input())
count = 0
for x in b:
  if(x == d):
    count += 1
print(count)
