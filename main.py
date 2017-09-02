#Binod Bhandari

import os
import sys
import _heapq

def prim(G, start_node):

    print("Running Prim's Algorithm")
    print("Starting Node: " + str(start_node))
    T = set()
    U = set()
    P = []

    vertices1 = []
    vertices2 = []
    vertices_list = []

    U.add(start_node)
    start = G[start_node]

    with open (filename, 'r') as textfile:
        firstLine = int (textfile.readline ())
        for line in textfile:
            vertices1.append (line.split (None, 1)[0])
            vertices2.append (line.split (None, 2)[1])

    for elem in range(firstLine):
        if elem not in vertices1:
            vertices_list.append (elem)

    _heapq.heappush(P,vertices_list)

    while len(U) != len(G):
        weight_of_every = []
        for elem in range(len (G)):
            for node in U:
                if elem not in U and (G[node][elem]):
                    weight_of_every.append((node,elem))

        sortedWeights = sorted(weight_of_every, key=lambda common_weight: G[common_weight[1]][common_weight[0]])
        print ("Added " + str(sortedWeights[0][1]))
        weight = (G[sortedWeights[0][0]][sortedWeights[0][1]])
        T.add(weight)
        T.add(sortedWeights[0])
        U.add(sortedWeights[0][1])
        edges = list((sortedWeights[0]))
        edges.sort()
        edges.append(weight)
        print ("Using Edge " + str(edges))

def kruskal(G):

    print("Running Kruskal's Algorithm")
    result = []
    node_visited = []
    node_visited.append(0)
    kruskal_item =[]


    while len(node_visited) != len (G):
        every_weight = []
        for elem in range (len (G)):
            for node in node_visited:
                if elem not in node_visited and (G[node][elem]) != 0:
                    every_weight.append ((node, elem))

        sortedWeights = sorted (every_weight,
                                key=lambda common_weight: G[common_weight[1]][common_weight[0]])

        weight = (G[sortedWeights[0][0]][sortedWeights[0][1]])
        result.append (sortedWeights[0])
        node_visited.append (sortedWeights[0][1])
        edges = list ((sortedWeights[0]))
        edges.sort ()
        edges.append(weight)
        kruskal_item.append(edges)

    kruskal_item.sort(key=lambda weight_kruskal:weight_kruskal[2])
    for item in kruskal_item:
        print ("Select Edge: " + str(item))

if __name__ == '__main__':

    weight_of_node = []
    vertices_list = []

    print("Welcome to Minimum Spanning Tree Finder")
    filename = input("Give the file name graph is in: ")

    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            firstLine = int(file.readline())
            for content in file:
                weight_of_node.append(content.split(None,3)[2])

        weight_of_node = [float(i) for i in weight_of_node]

        with open (filename, 'r') as file:
            next(file)
            G = [ ]
            for ver in range (0, firstLine):
                adj_matrix = [ ]
                for vert in range (0, firstLine):
                    if ver == vert:
                        adj_matrix.append (float (0))
                    else:
                        adj_matrix.append (float ('Inf'))
                G.append (adj_matrix)

            for content in file:
                vertices1, vertices2, weigh = content.split ()
                vertices1 = int (vertices1)
                vertices2 = int (vertices2)
                weigh = float (weigh)
                G[vertices1][vertices2] = G[vertices2][vertices1] = weigh

        print ("Commands: \n"
               "exit or ctrl-d - quits the program\n"
               "help - prints this menu\n"
               "prim integer_value - run's Prim's algorithm starting at node given\n"
               "kruskal - runs Kruskal's algorithm")

        while True:
            try:
                command = input ("Enter command: ")
            except EOFError:
                print("Bye")
                break

            if command == "exit":
                print("Bye")
                sys.exit (0)

            elif command == "help":
                print ("Commands: \n"
                       "exit or ctrl-d - quits the program\n"
                       "help - prints this menu\n"
                       "prim integer_value - run's Prim's algorithm starting at node given\n"
                       "kruskal - runs Kruskal's algorithm")

            elif command.split()[0] == "prim":
                startNode = int(command.split()[1])
                prim(G,startNode)

            elif command == "kruskal":
                kruskal(G)

            else:
                print("Wrong Command!!\n"
                      "Please type help for the Command list")
    else:
        print("Sorry file "+ filename + " can not be found.\n"
                                        "Please check your current directory and run it again")
