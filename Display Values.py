a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = {}
f = {}
g = []
e.update({a:b})
f.update({c:d})
print("First Dictionary")
print(e)
print("Second Dictionary")
print(f)
e.update(f)
print("Concatenated dictionary")
print(e)
print("The Values of Dictiionary")
g = list(e.values())
print(g)
