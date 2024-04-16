"""class node:
    def __init__(self,data):
        self.prev=None
        self.data = data
        self.next = None
class DLL:
    def __init__(self):
        self.head=None
    def createlist(self):
        n = int(input("enter the size"))
        for i in range(0,n):
            data = int(input("enter the data:"))
            self.insertend(data)
    def insertend(self,data):
        newnode=node(data)
        if self.head == None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        newnode.prev=temp
    def insertfront(self,data):
        newnode=node(data)
        if self.head!=None:
            newnode.next=self.head
            self.head=newnode
            newnode.next.prev=newnode

    def insertmiddle(self, pos,data):
        if pos == 0:
            self.insertfront(data)
            return
        newnode = node(data)
        temp = self.head
        for i in range(1, pos):
            if temp is None:
                print("position out of bound")
                return
            temp = temp.next
        if temp is None:
            print("position out of bound")
            return
        newnode.next = temp.next
        temp.next = newnode
        newnode.prev=temp
        newnode.next.prev=newnode

    def deletepos(self,pos):
        temp = self.head
        for _ in range(1, pos - 1):
            temp = temp.next
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
    def print(self):
        if self.head == None:
            print("empty list")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--->", end="")
                temp = temp.next
            print()


if __name__ == '__main__':
    l=DLL()
    l.createlist()
    l.print()
    insert=int(input("enter the number to inserted at first:"))
    l.insertfront(insert)
    l.print()
    insert2=int(input("enter the location to insert"))
    element=int(input("enter the element to be inserted"))
    l.insertmiddle(insert2,element)
    l.print()
    delete=int(input("enter the pos to be deleted"))
    l.deletepos(delete)
    l.print()
    l2=DLL()
    l2.createlist()
    l2.print()"""

class node:
    def __init__(self,data):
        self.prev=None
        self.data = data
        self.next = None
class DLL:
    def __init__(self):
        self.head=None
    def createlist(self):
        n = int(input("enter the size"))
        for i in range(0,n):
            data = int(input("enter the data:"))
            self.insertend(data)
    def insertend(self,data):
        newnode=node(data)
        if self.head == None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        newnode.prev=temp
    def insertfront(self,data):
        newnode=node(data)
        if self.head!=None:
            newnode.next=self.head
            self.head=newnode
            newnode.next.prev=newnode

    def insertmiddle(self, pos,data):
        if pos == 0:
            self.insertfront(data)
            return
        newnode = node(data)
        temp = self.head
        for i in range(1, pos):
            if temp is None:
                print("position out of bound")
                return
            temp = temp.next
        if temp is None:
            print("position out of bound")
            return
        newnode.next = temp.next
        temp.next = newnode
        newnode.prev=temp
        newnode.next.prev=newnode

    def deletepos(self,pos):
        temp = self.head
        for _ in range(1, pos - 1):
            temp = temp.next
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
    def print(self):
        if self.head == None:
            print("empty list")
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" ")
                temp = temp.next
            print()


if __name__ == '__main__':
    l=DLL()
    l.createlist()
    l.print()
    l2=DLL()
    l2.createlist()
    l2.print()




