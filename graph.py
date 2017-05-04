from random import randint
import copy
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

        self.number_of_edges=self.number_of_vertices*(self.number_of_vertices-1)/2*density/100

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
            return True
        else:
            return False
    def check_euler(self):
        euler=True
        if self.check_connectivity()==False:
            return False
        else:
            for i in range(1,self.number_of_vertices+1):
                if self.matrix[i].count(1)%2==1:
                    euler=False
                    break
            if euler:
                return True
            else:
                return False

    def delete_reverse_list(self,temp_list):
        for i in temp_list:
            if i[::-1] in temp_list:
                temp_list.remove(i[::-1])
    def print_list(self,temp_list):
        for i in temp_list:
            print(i)
    def copy_cycle_path(self,temp_list,hamilton):
        temp=[]
        for i in temp_list:
            if hamilton==1:
                if self.matrix[i[0]][i[-1]]==1:
                    temp.append(i)
            else:
                if i[0]==i[-1]:
                    temp.append(i)
        return temp

    def find_hamilton_path(self,vertice,visited=[],one_path=False):
        if one_path==False or self.capture_hamilton==False:
            visited.append(vertice)
            if len(visited)==self.number_of_vertices:
                self.hamilton_path.append(list(visited)) # list() copy the array, without it doesn`t work
                self.capture_hamilton=True
            for i in range(1,self.number_of_vertices+1):
                if self.matrix[vertice][i]==1 and i not in visited:
                    self.find_hamilton_path(i,visited,one_path)
            visited.pop()
    def hamilton(self,one_path=False):
        if self.check_connectivity()==True:
            print("Znalezone cykle Hamiltona: ")
            self.capture_hamilton=False
            self.hamilton_path=[]
            self.hamilton_cycles=[]

            for i in range(1,self.number_of_vertices+1):
                self.find_hamilton_path(i,[],one_path)

            self.hamilton_cycles=self.copy_cycle_path(self.hamilton_path,hamilton=1)
            self.delete_reverse_list(self.hamilton_cycles)
            self.print_list(self.hamilton_cycles)
        else:
            print("Brak cyklu Hamiltona")

    def find_euler_path(self,matrix,vertice,visited=[],one_path=False):
        if one_path==False or self.capture_euler==False:
            if len(visited)>=1:
                matrix[vertice][visited[-1]]=matrix[visited[-1]][vertice]=0
            visited.append(vertice)
            if len(visited)==self.number_of_edges+1:
                self.euler_paths.append(list(visited))
                self.capture_euler=True
            for i in range(1,self.number_of_vertices+1):
                if matrix[vertice][i]==1:
                    self.find_euler_path(copy.deepcopy(matrix),i,visited,one_path)
            visited.pop()
    def euler(self,one_path=False):
        if self.check_euler()==True:
            print("Znalezione cykle Eulera: ")
            self.capture_euler=False
            self.euler_paths=[]
            self.euler_cycles=[]

            for i in range(1,self.number_of_vertices+1):
                self.find_euler_path(copy.deepcopy(self.matrix),i,[],one_path)

            self.euler_cycles=self.copy_cycle_path(self.euler_paths,hamilton=0)
            self.delete_reverse_list(self.euler_cycles)
            self.print_list(self.euler_cycles)
