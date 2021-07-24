def GCD(a,b):
  c = []
  d = []
  e = []
  for x in range(2,a+1):
    if(a % x == 0):
      c.append(x)
  for x in range(2,b+1):
    if(b % x == 0):
      d.append(x)
  c = set(c)
  d = set(d)
  e = c.intersection(d)
  return(max(e))

a = int(input())
b = int(input())
c = GCD(a,b)
print("The GCD of the two numbers is",c)
