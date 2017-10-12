filejia=open(r"D:\朱烜宇\day13withoutcode\Emailjia.txt","r")
filejie=open(r"D:\朱烜宇\day13withoutcode\Emailjie.txt","w")
ch=True
while ch:
    ch=filejia.read(1)
    if ch:
        jiach=chr(ord(ch)-1)
        filejie.write(jiach)
filejie.close()
filejia.close()
