import re

# Pretend this is the file content
sample_text = """
Hello from muskan123@gmail.com, please contact test.user@domain.com or try admin@codealpha.tech
"""

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", sample_text)

print("Extracted Emails:")
for email in emails:
    print(email)