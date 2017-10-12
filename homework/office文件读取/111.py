import re
def get_email_list(text):
    pattern=re.compile("[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+")
    email_list=re.findall(pattern,text)
