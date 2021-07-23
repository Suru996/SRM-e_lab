#One Way
def count(c):
  return len(c)

a = input()
print("The number fo digits in the number are:",count(a))

#Another Way
def count(c):
  d = 0
  while(c > 0):
    d += 1
    c //= 10
  return d

a = int(input())
print("The number fo digits in the number are:",count(a))
