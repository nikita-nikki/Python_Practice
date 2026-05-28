# i = 0

# while i < 5:
#     if i == 2:
#         continue

#     i += 1

# when i == 2
# continue happens before increment
# infinite loop


''' Correctted one'''
i = 0

while i < 5:
    i += 1

    if i == 2:
        continue

    print(i)


''' While-else '''
x = 1

while x < 4:
    print(x)
    x += 1
else:
    print("Loop finished")

# here else will not work
x = 1

while x < 4:
    if x == 2:
        break
    print(x)
    x += 1
else:
    print("Finished")
