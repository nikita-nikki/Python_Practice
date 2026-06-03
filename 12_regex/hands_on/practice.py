# Regular Expressions (Regex) are patterns used to search, match, extract, validate, and replace text.

import re

''' re.search() '''
# Finds the first match anywhere in the string.

text = "My phone number is 9876543210"
match = re.search(r"\d+", text)
# \d → any digit (0-9)
# + → one or more occurrences
print(match)
# re.search() does not return the matched text directly.

# The Match object contains information such as:
# - what matched
# - where it matched
# - captured groups
print(match.group())


# if phone no. is not present in the text
import re
text = "Hello"
match = re.search(r"\d+", text)
print(match)
# match = None




''' re.findall() '''
# Returns all matches as a list.


text = "10 apples and 20 bananas"
print(re.findall(r"\d+", text))



'''re.match()'''
# Matches only from the start of the string.

print(re.match(r"Hello", "Hello World"))
print(re.match(r"World", "Hello World"))


''' re.sub()'''
# Replace matches.

text = "abc123xyz"
print(re.sub(r"\d+", "#", text))