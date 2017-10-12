import re
#m=re.search(r"^[1-9](\d{4,10})$","10499293")
#m=re.search(r"1[3,4,5,7,8](\d{9})","18003241579")
m=re.search(r"0[1-9](\d{1,2})-[1-9](\d{6,7})","0477-2247933")

if m!=1:
    print(m.group())
else:
    print("not find")
