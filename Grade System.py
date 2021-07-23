def grade(avg):
  if(avg >= 90):
    return("Grade:A")
  elif(avg > 70 and avg < 90):
    return("Grade:B")
  elif(avg > 50 and avg <= 70):
    return("Grade:C")
  else:
    return("Grade:D")
  
a = input().split()
b = len(a)
c = []
for x in range(0,b):
  c.append(int(a[x]))
d = sum(c) / b
f = grade(d)
print(f)
