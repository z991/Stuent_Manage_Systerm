import re
'''print(re.match("abc","abc"))
matchobj=re.match("abc","abcdefgabc")
print(matchobj)
print(matchobj.group(0))
line="libai is a boy not a girl"
matchobj=re.match(r"(.*) is (.*) not (.*)",line)
print(matchobj)
print(matchobj.group(3))'''
line="828587345734----347864dhkskfl"
matchobj=re.match(r"(.*)----(.*)",line)
print(matchobj)
print(matchobj.group(1))