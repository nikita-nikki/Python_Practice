#LIST COMPREHENSION

# [expression for item in iterable]

squares = [i * i for i in range(5)]
print("Squares:", squares)


nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
print("Even:", evens)


# [expr_if_true if condition else expr_if_false for item in iterable]
nums = [1, 2, 3, 4]
result = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(result)



# pairs = []
# for i in range(2):
#     for j in range(3):
#         pairs.append((i, j))
# print(pairs)

pairs = [(i, j) for i in range(2) for j in range(3)]
print(pairs)



#DICTIONARY COMPREHENSION
print("DICTIONARY COMPREHENSION")
# {key_expression: value_expression for item in iterable}
d = {i: i * i for i in range(5)}
print(d)

names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]
result = {name: score for name, score in zip(names, scores)}
print(result)