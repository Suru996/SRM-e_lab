name = input()
n = int(input())
file = open(name,'w+')
for x in range(0,n):
  a = input()
  file.writelines(a+'\n')
file = open(name)
print(file.read(),end='')
print("Number of lines:")
print(n)
