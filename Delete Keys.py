a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
key = int(input())
z = {}
x = {}
y = {}
w = {}
z.update({a:b})
x.update({c:d})
y.update({e:f})
w.update({g:h})
print("First Dictionary")
print(z)
print("Second Dictionary")
print(x)
print("Third Dictionary")
print(y)
print("Fourth Dictionary")
print(w)
z.update(x)
z.update(y)
z.update(w)
print("Concatenated dictionary is")
print(z)
if key in z.keys():
  print("Updated dictionary")
  print(z)
else:
  print("Key not found")
