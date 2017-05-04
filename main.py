from graph import graph


graphs=[]
for i in range(1000):
    graphs.append(graph(6,40))
    if graphs[-1].check_euler()==True:
        print(i)
        break
graph=graphs[-1]
graph.print_neighbours_list()


graph.hamilton()
graph.euler()
