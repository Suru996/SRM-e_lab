a = int(input())
b = []
odd = []
even = []
neg = []
for x in range(0,a):
  c = int(input())
  b.append(c)
for x in range(0,a):
  if(b[x] > 0 and b[x]%2 == 0):
    even.append(b[x])
  elif(b[x] > 0 and b[x]%2 != 0):
    odd.append(b[x])
  else:
    neg.append(b[x])
print("Sum of positive even numbers:",sum(even))
print("Sum of positive odd numbers:",sum(odd))
print("Sum of negative numbers:",sum(neg))
