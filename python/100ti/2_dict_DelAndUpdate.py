dict1={'a1':11,"a2":12}
dict2={'a3':11,"a4":22}
del dict1['a1']
print(dict2)
print(dict1)
dict2.update(dict1)
print(dict2)