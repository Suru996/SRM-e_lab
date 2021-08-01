a = int(input())
b = int(input())
sum_a = 0
sum_b = 0
for x in range(1,a):
  if(a % x == 0):
    sum_a += x
for x in range(1,b):
  if(b % x == 0):
    sum_b += x
if(sum_a == b and sum_b == a):
  print("Amicable")
else:
  print("Not Amicable")
