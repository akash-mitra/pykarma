import re

text = """
        I have received an email from someone@gmail.com in my
        email id (my_email@example.com), where I found that the
        the original email was actually forwarded from another
        address (unknown@hotmail.com)
        """

email_pattern = r'\w+@\w+.\w+'

emails = re.findall(email_pattern, text)

for email in emails:
    print(email)
