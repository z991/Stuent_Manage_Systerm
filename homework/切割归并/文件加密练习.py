file=open(r"D:\朱烜宇\day13withoutcode\Email.txt","r")
filejia=open(r"D:\朱烜宇\day13withoutcode\Emailjia.txt","w")
ch=True
while ch:
    ch=file.read(1)
    if ch:
        jiach=chr(ord(ch)+1)
        filejia.write(jiach)
file.close()
filejia.close()
