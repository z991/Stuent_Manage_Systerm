import re
regex=re.compile("\d{2}",re.IGNORECASE) #re.IGNORECASE忽略异常，忽略大小写
print(regex.match("9"))
