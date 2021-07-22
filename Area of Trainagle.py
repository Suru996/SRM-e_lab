import math
a = int(input())
b = int(input())
c = int(input())
s =(a + b + c) /2
area = math.sqrt(s*(s-1*(s-b)*(s-c))
print("The area of the triangle is",round(area,1))
