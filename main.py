from graph import graph
import time

graph=graph(12,0)
graph.print_neighbours_list()

start=time.time()
graph.hamilton()
print("hamilton",time.time()-start)

start=time.time()
graph.euler()
print("euler",time.time()-start)
