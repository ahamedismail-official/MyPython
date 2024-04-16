class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class cll:
    def __init__(self):
        self.head=None

    def createlist(self):
        n = int(input("enter the size"))
        for i in range(n):
            data = int(input("enter the data:"))
            self.insertend(data)
    def insertend(self,data):
        nn=node(data)
        if self.head is None:
            self.head=nn
            nn.next=self.head
            return
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=nn
        nn.next=self.head

    def insertbegin(self, data):
        nn = node(data)
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=nn
        nn.next=self.head
        self.head=nn
    def insertmiddle(self, data, pos):
        nu = node(data)
        temp = self.head
        for i in range(1,pos-1):
            temp=temp.next
        nu.next = temp.next
        temp.next = nu

    def deletebegin(self):
        temp = self.head
        self.head = temp.next
    def print(self):
        c=0
        if self.head == None:
            print("empty list")
        else:
            temp = self.head
            while temp.next!=self.head:
                c=c+1
                print(temp.data, "--->", end="")
                temp = temp.next
            print(temp.data)
            c+=1
            print(c)
if __name__ == '__main__':
    l = cll()
    l.createlist()
    l.print()
    l.insertbegin(5)
    l.print()
    l.insertmiddle(2,3)
    l.print()
    l.deletebegin()
    l.print()
