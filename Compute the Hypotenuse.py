import math
def hyp(a,b):
  c = math.sqrt(a ** 2 + b ** 2)
  return round(c)

a = int(input())
b = int(input())
print(hyp(a,b))
