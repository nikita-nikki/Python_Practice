"""
REGULAR EXPRESSIONS ASSIGNMENT

"""

import re


# 1. Extract Email Addresses


print("1. Extract Email Addresses")

text = "Contact us at support@test.com or admin123@gmail.com"

emails = re.findall(
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    text
)

print("Emails:", emails)



# 2. Validate Password


print("\n2. Validate Password")

password = "Password@123"

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!]).{8,}$'

if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")


# 3. Extract Dates


print("\n3. Extract Dates")

text = "Meeting on 12-05-2026 and another on 2026-06-01 and 15/07/2026"

dates = re.findall(
    r'\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}-\d{2}-\d{2})\b',
    text
)

# \b -  word boundary is a position where a word starts or ends.
# (?:pattern) It means: "Group these regex parts together, but don't save the matched text as a capture group."
print("Dates:", dates)



# 4. Find Duplicate Words


print("\n4. Find Duplicate Words")

text = "This is is a sample sample text."

duplicates = re.findall(r'\b(\w+)\s+\1\b', text)

print("Duplicate Words:", duplicates)



# 5. Convert Multiple Spaces to One


print("\n5. Convert Multiple Spaces to One")

text = "Hello     World\t\tPython"

result = re.sub(r'[\t ]+', ' ', text)

print("Before :", repr(text))
print("After  :", result)


# 6. Log File Parser


print("\n6. Log File Parser")

logs = """
2026-06-01 10:23:45 ERROR Database connection failed
2026-06-01 10:24:12 INFO User login successful
"""

pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w+)\s+(.*)'

parsed_logs = []

for line in logs.strip().split("\n"):
    match = re.match(pattern, line)

    if match:
        parsed_logs.append({
            "timestamp": match.group(1),
            "log_level": match.group(2),
            "message": match.group(3)
        })

print("Parsed Logs:")
for log in parsed_logs:
    print(log)



# 7. Extract HTML Tags


print("\n7. Extract HTML Tags")

html = """
<div>Hello</div>
<p>World</p>
<a href="#">Link</a>
"""

tags = re.findall(r'<([a-zA-Z][a-zA-Z0-9]*)\b', html)

print("Tags:", tags)


# 8. Extract Currency Values


print("\n8. Extract Currency Values")

text = "Revenue was $1,200.50, profit ₹50,000 and loss €300"

currencies = re.findall(
    r'[$₹€]\d[\d,]*(?:\.\d+)?',
    text
)

print("Currency Values:", currencies)