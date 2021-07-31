a = {'Toolname':'eLab','Launch':2017,'State':'Tamilnadu','Country':'Ind'}
b = input()
c = input()
for x in a.values():
  print(x)
a.update({b:c})
print(a[b])
