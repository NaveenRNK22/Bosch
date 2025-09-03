class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self): 
        self.head = None

    def InsertBegin(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head=new_node

        else:
            new_node.next = self.head
            self.head = new_node
            
    
    def InsertIndex(self,data,index):

        if index == 0:
            self.Insertbegin(data)
            return
        else:
            position = 0
            current_node = self.head
            while (current_node != None and position+1 != index):

                if current_node != None:
                    new_node = Node(data)
                    new_node.next = current_node.next
                    current_node.next = new_node

                else:
                    print("Index not present, Linking at end")
                    current_node = new_node

                position += 1 
                current_node = current_node.next

    def push(self,data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node


    def Deletion(self,val):
        current_node = self.head
        while current_node !=None:
            if current_node.data == val:
                prev_node.next = current_node.next
                current_node = None
                break
            prev_node = current_node
            current_node = current_node.next

    
    def printList(self):
        temp = self.head
        while temp:
            print (temp.data,"->",end='')
            temp= temp.next
        print("")


Llist = LinkedList()

Llist.InsertBegin(3)
Llist.InsertBegin(9)
Llist.InsertBegin(8)
Llist.printList()
Llist.InsertIndex(5,2)
Llist.push(6)
Llist.InsertIndex(7,2)
Llist.printList()

Llist.Deletion(3)
Llist.printList()
