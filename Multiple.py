a = {}
g = {}
f = {}
b = int(input())
c = int(input())
d = int(input())
e = int(input())
a.update({b:c})
f.update({d:e})
g.update(a)
g.update(f)
print("First Dictionary")
print(a)
print("Second Dictionary")
print(f)
print("Concatenated Dictionary")
print(g)
print("Total sum of values in the dictionary")#Product actually but have to print this way
sum = 1
for x in g:
  sum *= g[x]
print(sum)
