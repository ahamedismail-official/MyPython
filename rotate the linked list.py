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

