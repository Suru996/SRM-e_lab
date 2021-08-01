a = int(input())
d = a
sum = 0
if(d > 0):
  while(d):
    r = d % 10
    e = 1
    for x in range(1,r+1):
      e *= x
      sum += e
      d = int(d / 10)
    if(sum == a):
      print("The number is a strong number")
    else:
      print("The number is not a strong number")
