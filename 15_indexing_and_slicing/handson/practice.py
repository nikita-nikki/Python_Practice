"""
INDEXING, SLICING & REVERSE INDEXING PRACTICE
Run this file section by section and observe the output.
"""


# 1. BASIC INDEXING


text = "Python"

print("Original String:", text)

print("First character:", text[0])
print("Second character:", text[1])
print("Last character:", text[-1])
print("Second last character:", text[-2])


# 2. INDEXING WITH LISTS


numbers = [10, 20, 30, 40, 50]

print("\nList:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])


# 3. BASIC SLICING
# Syntax: sequence[start:end:step]


print("\nSLICING EXAMPLES")

print("text[0:3] =", text[0:3])      # Pyt
print("text[:4]  =", text[:4])       # Pyth
print("text[2:]  =", text[2:])       # thon
print("text[:]   =", text[:])        # entire string


# 4. STEP SLICING


print("\nSTEP SLICING")

word = "ABCDEFGHIJ"

print("word[::2]  =", word[::2])
print("word[1::2] =", word[1::2])
print("word[::3]  =", word[::3])


# 5. REVERSE INDEXING


print("\nREVERSE INDEXING")

name = "Developer"

print("Last character:", name[-1])
print("Second last:", name[-2])
print("Third last:", name[-3])


# 6. REVERSING USING SLICING


print("\nREVERSING")

print("Original:", name)
print("Reversed:", name[::-1])


# 7. NEGATIVE SLICING


print("\nNEGATIVE SLICING")

print("name[-5:] =", name[-5:])
print("name[:-3] =", name[:-3])
print("name[-7:-2] =", name[-7:-2])

# 8. EDGE CASE - INDEX OUT OF RANGE


print("\nEDGE CASE: INDEX OUT OF RANGE")

try:
    print(text[100])
except IndexError as e:
    print("Error:", e)


# 9. EDGE CASE - SLICING OUT OF RANGE
# Slicing never raises IndexError


print("\nEDGE CASE: SLICING OUT OF RANGE")

print(text[0:100])
print(text[100:200])
print(text[-100:100])

# =====================================================
# 10. EDGE CASE - EMPTY SLICE
# =====================================================

print("\nEDGE CASE: EMPTY SLICE")

print(text[3:3])    # ''
print(text[5:2])    # ''

# =====================================================
# 11. EDGE CASE - STEP = 0
# =====================================================

print("\nEDGE CASE: STEP = 0")

try:
    print(text[::0])
except ValueError as e:
    print("Error:", e)

# =====================================================
# 12. NEGATIVE STEP
# =====================================================

print("\nNEGATIVE STEP")

print(text[::-1])
print(text[::-2])
print(text[4:1:-1])

# =====================================================
# 13. LIST SLICING
# =====================================================

fruits = ["apple", "banana", "mango", "orange", "grapes"]

print("\nLIST SLICING")

print(fruits[1:4])
print(fruits[::-1])
print(fruits[-3:])
print(fruits[:-2])

# =====================================================
# 14. NESTED LIST INDEXING
# =====================================================

nested = [10, [20, 30, 40], 50]

print("\nNESTED LIST INDEXING")

print(nested[1])
print(nested[1][0])
print(nested[1][-1])

# =====================================================
# 15. TUPLE INDEXING & SLICING
# =====================================================

t = (100, 200, 300, 400, 500)

print("\nTUPLE")

print(t[0])
print(t[-1])
print(t[1:4])

# =====================================================
# 16. STRING PALINDROME CHECK USING SLICING
# =====================================================

print("\nPALINDROME CHECK")

word = "madam"

if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

# =====================================================
# 17. IMPORTANT EDGE CASES
# =====================================================

print("\nIMPORTANT EDGE CASES")

s = "HELLO"

# Start > End with positive step
print(s[4:1])       # ''

# Start < End with negative step
print(s[1:4:-1])    # ''

# Reverse complete string
print(s[::-1])      # OLLEH

# Reverse from index 4 to 1
print(s[4:1:-1])    # OLL

# Huge indexes
print(s[100:500])   # ''
print(s[-500:500])  # HELLO

# =====================================================
# 18. INTERVIEW PRACTICE QUESTIONS
# =====================================================

print("\nPRACTICE")

sample = "PROGRAMMING"

print("sample[-1]    =", sample[-1])
print("sample[::-1]  =", sample[::-1])
print("sample[2:8]   =", sample[2:8])
print("sample[-5:-1] =", sample[-5:-1])
print("sample[::2]   =", sample[::2])
print("sample[::-2]  =", sample[::-2])


