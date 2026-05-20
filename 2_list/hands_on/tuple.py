company = ("milton", "cello", "borosil")
size = (100, 500,1000)

"type"
print(type(company))
print(type(size))

"size"
print(len(company))

"iteration"
for bottle in company:
    print(bottle)

"immutability"
'''
 size[0] = 200
 it throws error because value of tuple cannot be changed
 '''