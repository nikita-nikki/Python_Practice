# =========================
# Part 1 — List Operations
# =========================

my_list = [1, 33, 56, 1001, 768]
print("Initial List:", my_list)

# 1. Add 89 to the end of the list
my_list.append(89)
print("After adding 89 at end:", my_list)

# 2. Add 39 to the beginning of the list
my_list.insert(0, 39)
print("After adding 39 at beginning:", my_list)

# 3. Add elements of another list [77,66,44] into the existing list
my_list.extend([77, 66, 44])
print("After extending [77,66,44]:", my_list)

# 4. Add [99,88] as a single nested element inside the list
my_list.append([99, 88])
print("After adding nested list [99,88]:", my_list)

# 5. Insert 'Apple' at position 2
my_list.insert(2, 'Apple')
print("After inserting 'Apple' at position 2:", my_list)

# 6. Replace 'Apple' with 'Pineapple'
apple_index = my_list.index('Apple')
my_list[apple_index] = 'Pineapple'
print("After replacing 'Apple' with 'Pineapple':", my_list)

# 7. Remove the element present at position 4
my_list.pop(4)
print("After removing element at position 4:", my_list)

# 8. Remove 'Pineapple' from the list
my_list.remove('Pineapple')
print("After removing 'Pineapple':", my_list)


# =========================
# Part 2 — Pair Sum Problem
# =========================

numbers = [1,2,3,4,5,6,7,8]
z = 9

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == z:
            pairs.append((numbers[i], numbers[j]))

final_output = tuple(pairs)

print("\nPairs whose sum is", z, ":")
print(final_output)