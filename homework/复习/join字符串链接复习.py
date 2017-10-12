#print("-".join("abcdefg"))
#print("-".join("abcdefg"))
#print("----".join("abc defg"))  #"abcdefg"每个字符串之间每两个字符之间插入一个字符串间隔
#print(len("sadsadsad")) #求长度

#for  i  in  range(5,50):
    #print("8888".rjust(i,'-')) #i长度，左边填充*   8888在右边
    #print("8888".ljust(i,"*"))#i长度，右边填充*  8888在左边
for i in range(5,50):
    #print("8888".rjust(i,'-'))
    print("8888".ljust(i,'*'))