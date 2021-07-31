a = int(input())
b = []
c = []
e = {}
for x in range(0,a):
  d = int(input())
  b.append(d)
for x in range(0,a):
  d = int(input())
  c.append(d)
key = int(input())
for x in range(0,a):
  e.update({b[x]:c[x]})
print("The dictionary is")
print(e)
if key in e.keys():
  print("True")
 else:
  print("False")
