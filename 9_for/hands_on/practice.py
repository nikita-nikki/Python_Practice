for i in range(5, 1):
    print(i)

print("Done")
# Since 5 < 1 is already false, loop never runs.



for i in range(5):
    print(i)
    i = 100

print(i)
# Loop assignment happens every iteration, but after loop ends, i remains 100


for i in range(3):
    if i == 1:
        break
else:
    print("Finished")

print("Done")