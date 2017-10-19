class d_linked_node:
    
    def __init__(self, initData, initNext, initPrevious):
        # constructs a new node and initializes it to contain 
        # the given object (initData) and links to the given next 
        # and previous nodes. 
        self.__data = initData
        self.__next = initNext
        self.__previous = initPrevious
        if (initPrevious != None):
            initPrevious.__next = self
        if (initNext != None):
            initNext.__previous = self
    
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next
    
    def getPrevious(self):
        return self.__previous
    
    def setData(self, newData):
        self.__data = newData
    
    def setNext(self, newNext):
        self.__next= newNext
    
    def setPrevious(self, newPrevious):
        self.__previous= newPrevious    