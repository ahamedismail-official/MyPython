class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top=None

    def ifempty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, data):

        if self.top == None:
            self.top = node(data)

        else:
            newnode = node(data)
            newnode.next = self.top
            self.top = newnode

    def pop(self):

        if self.ifempty():
            return None

        else:

            popnode = self.top
            self.top = self.top.next
            popnode.next = None
            return popnode.data

    def peek(self):

        if self.ifempty():
            return None

        else:
            return self.top.data



    def display(self):

        iternode = self.top
        if self.ifempty():
            print("Stack Underflow")

        else:

            while (iternode != None):

                print(iternode.data, end="")
                iternode = iternode.next
                if (iternode != None):
                    print(" -> ", end="")
            return
        print()


if __name__ == "__main__":
    s = stack()

    s.push(11)
    s.push(22)
    s.push(33)
    s.push(44)
    s.display()
    s.pop()
    s.display()
    print("\n",s.peek())
