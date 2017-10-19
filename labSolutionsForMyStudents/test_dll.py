# Testing code for Assignment #3 Exercise 2

# Expected output:

'''
F->B->E->A->C->D
D<-C<-A<-E<-B<-F
The DLL contains 6 nodes
F
B->E->A->C
C<-A<-E<-B
C
A
E
B
'''

from doubly_linked_list import Doubly_Linked_List

dll = Doubly_Linked_List()
dll.add("A")
dll.add("B")
dll.append("C")
dll.append("D")
dll.insert(1, "E")
dll.insert(0, "F")
print(dll)
print(dll.reverse_string())
print("The DLL contains", dll.size(), "nodes")
print(dll.pop(0))
dll.remove("D")
print(dll)
print(dll.reverse_string())
while not dll.is_empty():
    print(dll.pop())



