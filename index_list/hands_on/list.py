digits = [0,1,2,3,4,5,6,7,]

print(digits[0])  
print(digits[1]) 

digits.append(9)
print(digits)

count = digits.count(6)
print(count)

print(type(count))
print(type(digits))

digits.insert(3, 10)
"inser(index, value)"
print(digits)