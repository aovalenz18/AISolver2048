class Block(object):
    def __init__(self, index, value):
        super(Block, self).__init__()
        self.index = index
        self.value = value
    
    def getIndex(self):
        return self.index
    
    def setIndex(self,index):
        self.index = index
    
    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value = value
    
    
    
    
        