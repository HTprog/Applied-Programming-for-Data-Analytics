from collections import defaultdict

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = []

    def addNeighbor(self,nbr):
        self.connectedTo.append(nbr)

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList =defaultdict(list)
        self.numVertices = 0

    def __contains__(self,n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def Add(self,item):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(item)
        self.vertList[item] = newVertex
        return newVertex

    def Search(self,item):
        if item in self.vertList:
            return print(True)
        else:
            return print(False)


    def AddEdges(self,item1,item2):
        if item1 not in self.vertList:
            nv = self.Add(item1)
        if item2 not in self.vertList:
            nv = self.Add(item2)
        self.vertList[item1].addNeighbor(self.vertList[item2])

    def getVertices(self):
        return print(list(self.vertList))

    def getEdges(self,m):
        connectedtolist=[]
        for i in self.vertList[m].getConnections():
            connectedtolist.append(i.getId())
        print(m,'is connected to',connectedtolist)

    def Size(self):
        return print(self.numVertices)

    def isPath(self,m,n):
        visited = [False] * self.numVertices
        queue= []
        queue.append(m)
        visited[m] = True

        while queue:
            m = queue.pop(0)
            if m==n:
                return print(True)
            else:
                for i in self.vertList[m].getConnections():
                    if visited[i.getId()] == False:
                        queue.append(i.getId())
                        visited[i.getId()] = True
        return print(False)


    def findAllPathsUtil(self, m, n, visited, path):
        visited[m]= True
        path.append(m)
        if m == n:
            print (path,end=" ")
        else:
            for i in self.vertList[m].getConnections():
                if visited[i.getId()]== False:
                    self.findAllPathsUtil(i.getId(), n, visited, path)
        path.pop()
        visited[m]= False

    def findAllpath(self,m,n):
        visited =[False]*(self.numVertices)
        path = []
        self.findAllPathsUtil(m, n, visited, path)



    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbour in self.vertList[v].getConnections():
            if visited[neighbour.getId()] == False:
                if self.isCyclicUtil(neighbour.getId(), visited, recStack) == True:
                    return True
            elif recStack[neighbour.getId()] == True:
                return True

        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * (self.numVertices + 1)
        recStack = [False] * (self.numVertices + 1)
        for node in range(self.numVertices):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    print("")
                    return print(True)
        print("")
        return print(False)


    def DFSUtil(self, temp, v, visited):
        visited[v] = True
 
        temp.append(v)
 
        for i in self.vertList[v].getConnections():
            if visited[i.getId()] == False:
 
                temp = self.DFSUtil(temp, i.getId(), visited)
        return temp

    def allConnected(self):
        visited = []
        cc = []
        for i in range(self.numVertices):
            visited.append(False)
        for v in range(self.numVertices):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        if len(cc)!=1:
            print("")
            return print(False)
        else:
            print("")
            return print(True)

print('Part A')
g = Graph()
g.Add(4)
g.AddEdges(0,1)
g.AddEdges(0,2)
g.AddEdges(1,2)
g.AddEdges(2,3)

g1 = Graph()
g1.Add(4)
g1.AddEdges(0,2)
g1.AddEdges(1,3)

g.isPath(1,3)
g1.isPath(1,3)

print('Part B')
g3 = Graph()
g3.Add(5)
g3.AddEdges(1,0)
g3.AddEdges(1,2)
g3.AddEdges(2,0)
g3.AddEdges(0,3)
g3.AddEdges(3,4)

g4 = Graph()
g4.Add(3)
g4.AddEdges(0,1)
g4.AddEdges(1,2)
g.isCyclic()
g1.isPath(1,3)
