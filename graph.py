"""import numpy as np
a = np.array([[1, 2, 3],[4,5,6],[7,8,9]])
print(a)"""

# Adjacency Matrix representation in Python


class Graph(object):


    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size


    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1


    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size


    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print()


def main():
    n=int(input("No of Vertices:"))
    g = Graph(n)
    for i in range(1,n+1):
        for j in range(1,n+1):
            op=int(input())
            if op==1:
                g.add_edge(i,j)

    g.print_matrix()


if __name__ == '__main__':
    main()