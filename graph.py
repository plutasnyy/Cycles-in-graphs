from random import randint
from itertools import permutations
class graph(object):

    def find_non_empty_index(self):
        x,y=0,0
        x_counter,y_counter=1,1
        temp=self.number_of_vertices
        while (self.matrix[x][y]==0 or x_counter<=1 or y_counter<=1):
            x,y=randint(1,temp),randint(1,temp)
            x_counter=self.matrix[x].count(1)
            y_counter=self.matrix[y].count(1)
        return x,y
    def create_full_graph(self):
        for i in range(0,self.number_of_vertices+1):
            X=[]
            for j in range(0,self.number_of_vertices+1):
                if j*i==0 or j==i:
                    X.append(0)
                else:
                    X.append(1)
            self.matrix.append(X)
    def delete_edges(self,density):
        full_count_edges=self.number_of_vertices*(self.number_of_vertices-1)/2
        for i in range(int(full_count_edges*(100-density)/100)):
            x,y=self.find_non_empty_index()
            self.matrix[x][y]=self.matrix[y][x]=0
    def __init__(self,number_of_vertices,density):
        #minimum destinity -> n*(n-1)/2*d>=n-1
        #is equal to d>=2/n

        if density<200/number_of_vertices:
            density=200/number_of_vertices

        self.matrix=[]
        self.number_of_vertices=int(number_of_vertices)

        self.create_full_graph()
        self.delete_edges(density)

    def print_neighbours_list(self):
        for i in range(1,self.number_of_vertices+1):
            X=[x for x in range(len(self.matrix[i])) if self.matrix[i][x]]
            print(i,X)

    def check_connectivity(self):
        connected=True
        for i in range(1,self.number_of_vertices+1):
            if self.matrix[i].count(1)==0:
                connected=False
                break
        if connected==True:
            print("Graf jest spojny")
            return True
        else:
            print("Graf nie jest spojny")
            return False
    def check_euler(self):
        euler=True
        if self.check_connectivity()==False:
            print("Graf nie ma cyklu Eulera")
            return False
        else:
            for i in range(1,self.number_of_vertices+1):
                if self.matrix[i].count(1)%2==1:
                    euler=False
                    break
            if euler:
                print("Graf ma cykl Eulera")
                return True
            else:
                print("Graf nie ma cyklu Eulera")
                return False

    def find_hamilton_path(self,vertice,visited=[]):
        visited.append(vertice)
        if len(visited)==self.number_of_vertices:
            self.hamilton_path.append(list(visited)) # list() copy the array, without it doesn`t work

        for i in range(1,self.number_of_vertices+1):
            if self.matrix[vertice][i]==1 and i not in visited:
                self.find_hamilton_path(i,visited)
        visited.pop()

    def hamilton(self):
        self.hamilton_path=[]
        for i in range(1,self.number_of_vertices+1):
            self.find_hamilton_path(i)
        print(self.hamilton_path)
