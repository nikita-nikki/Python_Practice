# Frequency Counter Using Sets + Lists


data = [1, 2, 2, 3, 4, 4, 4, 5]

# 1. Unique values
unique_values = set(data)
print("Unique values:", unique_values)

# 2. Duplicate values
duplicate_values = set()

for item in data:
    if data.count(item) > 1:
        duplicate_values.add(item)

print("Duplicate values:", duplicate_values)

# 3. Frequency of each value
frequency = {}

for item in unique_values:
    frequency[item] = data.count(item)

print("Frequency of each value:", frequency)