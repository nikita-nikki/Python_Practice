d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}


# Merge Dictionaries


merged = {**d1, **d2}

print("Merged Dictionary:")
print(merged)



# Sort by Key


sort_by_key = dict(sorted(merged.items()))

print("\nSorted by Key:")
print(sort_by_key)



# Sort by Value


sort_by_value = dict(
    sorted(merged.items(), key=lambda item: item[1])
)

print("\nSorted by Value:")
print(sort_by_value)