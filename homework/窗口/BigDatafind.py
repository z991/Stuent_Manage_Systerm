import codecs

class bigdatafind:
    def __init__(self):
        self.file=codecs.open(path,"rb","GBK","ignore")
        pass
    def find(self,searchstr):
        while True:
            line=self.file.readline()
            if line.find(searchstr)!=-1:
                print(line,end="")
            if not line:
                break


        pass
    def show(self):
        pass