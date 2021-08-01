n = int(input())#Length of list
b = []
for x in range(0,n):
  a = int(input())# input from user
  b.append(a)#Assigning each value given by user as integer type
k = int(input())#Multiples of k
for x in range(0,n):
  if(b[x] % k ==0):
    print(b[x])
