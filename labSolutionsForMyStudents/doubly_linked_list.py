class Double_Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.prev
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNext):
        self.next= newNext
    
    def setPrevious(self, newPrevious):
        self.prev= newPrevious
        
class Doubly_Linked_List:
    
    # creates a new doubly linked list
    # head and tail are initialized to None
    def __init__(self):
        self.head=None 
        self.tail=None
        self.__size=0
    
    # adds a new node with data = item to the beginning of the list    
    def add(self, item):
        temp = Double_Node(item)
        if (self.tail == None):
            self.head = temp
            self.__size += 1            
            self.tail = temp
        else:
            temp.setNext(self.head)            
            self.head.setPrevious(temp)
            self.head = temp
            self.__size += 1
    
    # adds a new node with data = item to the end of the list    
    def append(self, item):
        if self.__size == 0:
            self.add(item)
        else:
            self.__size +=1
            temp = Double_Node(item)
            temp.setPrevious(self.tail)
            self.tail.setNext(temp)
            self.tail = temp
        
    # insert a new node with data = item at the given position
    # assume index is a valid position to insert at
    def insert(self, index, item):
        temp = self.head
        temp_in = Double_Node(item)
        for i in range(index):
            temp = temp.getNext()        
        if (index == 0):
            temp_in.setNext(self.head)
            self.head = temp_in
            if (self.__size == 0):
                self.tail = temp_in
            else:
                temp_in.getNext().setPrevious(temp_in)
            self.__size +=1
        else:
            if (temp == None):
                temp_in.setPrevious(self.__tail)
                self.tail.setNext(temp_in)
                self.tail=temp_in
            else:
                temp_in.setNext(temp)
                temp.getPrevious().setNext(temp_in)
                temp_in.setPrevious(temp.getPrevious())
                temp.setPrevious(temp_in)
            self.__size +=1
    
    # removes and returns the element at the specified index 
    # assume the index is a valid position to remove at
    # default value indicates to pop from the end of the list
    def pop(self, index=-1):
        if index == -1:
            temp = self.tail
            if (self.__size < 2):
                self.head = None
                self.tail = None
                self.__size = 0
            else:            
                temp.getPrevious().setNext(None)
                self.tail = temp.getPrevious()
                self.__size -= 1          
            return temp.getData()
        else:
            self.__size -= 1
            temp = self.head
            if (index == 0):
                self.head = temp.getNext()
                if(self.head == None):
                    self.tail = None
                else:
                    self.head.setPrevious(None)
                return temp.getData()
            else:
                for i in range(index):
                    temp = temp.getNext()
                a = temp.getPrevious()
                a.setNext(temp.getNext())
                if (a.getNext() == None):
                    self.tail = a
                else:
                    a.getNext().setPrevious(a)
                return temp.getData()
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
            index = -1
        return index
    # removes the first node with data = item from the list
    # do nothing if item is not in the list
    def remove(self, item):
        if (self.search(item)):
            inde = self.index(item)
            self.__size -= 1
            temp = self.head
            if (inde == 0):
                self.head = temp.getNext()
                if(self.head == None):
                    self.tail = None
                else:
                    self.head.setPrevious(None)
            else:
                for i in range(inde):
                    temp = temp.getNext()
                a = temp.getPrevious()
                a.setNext(temp.getNext())
                if (a.getNext() == None):
                    self.tail = a
                else:
                    a.getNext().setPrevious(a)
        
    # returns the size of the doubly linked list
    def size(self):
        size = self.__size
        return size
        
    # returns True if the doubly linked list is empty, False otherwise
    def is_empty(self):
        if self.__size == 0:
            return True
        else:
            return False

    # returns a string representation of the list, from head to tail
    # each piece of data is separated by "->"
    def __str__(self):
        output = []
        current = self.head
        while current:
            output.append(current.getData())
            current = current.getNext()
        return "->".join(output)    
        
    # returns a string representation of the list, from tail to head
    # each piece of data is separated by "<-"
    def reverse_string(self):
        output = []
        current = self.tail
        while current:
            output.append(current.getData())
            current = current.getPrevious()
        return "<-".join(output)
                 
class Queue:
    def __init__(self):
        self.items = Doubly_Linked_List()
    
    def enqueue(self, item):
        self.items.add(item)
    
    def dequeue(self):
        self.items.pop()
                 
                 