import re

# Sample text containing email addresses
text = """
Contact us at student@gmail.com
For support, email admin@college.edu
Invalid email: student@.com
Another email: teacher123@yahoo.com
"""

# Regular expression pattern for email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Find all email addresses
emails = re.findall(pattern, text)

# Display the results
print("Email addresses found:")

for email in emails:
    print(email)