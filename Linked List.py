class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class sll:
    def __init__(self):

        self.head = None

    def createlist(self):
        n = int(input("enter the size"))
        for i in range(n):
            data = int(input("enter the data:"))
            self.insertend(data)

    def insertend(self, data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    def search(self,data):


        current = self.head

        while current != None:
            if current.data ==data:

                return True

            current = current.next



        return False

    def print(self):
        if self.head == None:
            print("empty list")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--->", end="")
                temp = temp.next

if __name__ == '__main__':
    l = sll()
    l.createlist()
    if l.search(5):
        print("Yes")
    else:
        print("No")
    l.print()

"""
class node:
    def _init_(self, data):
        self.data = data
        self.next = None
class sll:
    def _init_(self):
        self.head = None

    def createlist(self):
        n = int(input("enter the size"))
        for i in range(n):
            data = int(input("enter the data:"))
            self.insertend(data)

    def insertbegin(self, data):
        nn = node(data)
        nn.next = self.head
        self.head = nn

    def insertmiddle(self, data, pos):
        if pos==0:
            self.insertbegin(data)
            return
        nu = node(data)
        temp = self.head
        for i in range(1,pos):
            if temp is None:
                print("position out of bound")
                return
            temp = temp.next
        if temp is None:
            print("position out of bound")
            return
        nu.next = temp.next
        temp.next = nu

    def insertend(self, data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
    def deletebegin(self):
        temp=self.head
        self.head=temp.next
    def deletemiddle(self,pos):
        temp=self.head
        for _ in range(1,pos-1):
            temp=temp.next
        temp.next=temp.next.next
    def deleteend(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None

    def print(self):
        c=0
        if self.head == None:
            print("empty list")
        else:
            temp = self.head
            while temp:
                c=c+1
                print(temp.data, "--->", end="")
                temp = temp.next
            print()
            print(c)
    def  search(self,data):
        temp=self.head
        while temp:
            if temp.data==data:
                print("element is present")
                return
            temp=temp.next
l = sll()
l.createlist()
l.insertbegin(50)
l.insertmiddle(70, 3)
l.print()
l.search(70)"""


