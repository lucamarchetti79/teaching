from collections import deque
import math

class DiGraphLL:
    def __init__(self):
        """Every node is an element in the dictionary. 
        The key is the node id and the value is a dictionary
        with second node as key and the weight as value
        """
        self.__nodes = dict()
        
    def insertNode(self, node):
        test = self.__nodes.get(node, None)
        
        if test == None:
            self.__nodes[node] = {}
            #print("Node {} added".format(node))
    
    def insertEdge(self, node1, node2, weight):
        test = self.__nodes.get(node1, None)
        test1 = self.__nodes.get(node2, None)
        if test != None and test1 != None:
            #if both nodes exist othewise don't do anything
            test = self.__nodes[node1].get(node2, None)
            if test != None:
                exStr = "Edge {} --> {} already existing.".format(node1,node2)
                raise Exception(exStr)
            else:    
                #print("Inserted {}-->{} ({})".format(node1,node2,weight))
                self.__nodes[node1][node2] = weight
        
    
    def deleteNode(self, node):
        test = self.__nodes.get(node, None)
        if test != None:
            self.__nodes.pop(node)
        # need to loop through all the nodes!!!
        for n in self.__nodes:
            test = self.__nodes[n].get(node, None)
            if test != None:
                self.__nodes[n].pop(node)
    
    def deleteEdge(self, node1,node2):
        test = self.__nodes.get(node1, None)
        if test != None:
            test = self.__nodes[node1].get(node2, None)
            if test != None:
                self.__nodes[node1].pop(node2)
                
    def __len__(self):
        return len(self.__nodes)
    
    def nodes(self):
        return list(self.__nodes.keys())
    
    def graph(self):
        return self.__nodes
    
    def __str__(self):
        ret = ""
        for n in self.__nodes:
            for edge in self.__nodes[n]:           
                ret += "{} -- {} --> {}\n".format(str(n),
                                                  str(self.__nodes[n][edge]),
                                                  str(edge))
        return ret
    
    def adjacent(self, node):
        """returns a list of nodes connected to node"""
        ret = []
        test = self.__nodes.get(node, None)
        if test != None:
            for n in self.__nodes:
                if n == node:
                    #all outgoing edges
                    for edge in self.__nodes[node]:
                        ret.append(edge)
                else:
                    #all incoming edges
                    for edge in self.__nodes[n]:
                        if edge == node:
                            ret.append(n)
            
        return ret

    def adjacentEdge(self, node, incoming = True):
        """
        If incoming == False
        we look at the edges of the node
        else we need to loop through all the nodes. 
        An edge is present if there is a 
        corresponding entry in the dictionary.
        If no such nodes exist returns None
        """
        ret = []
        if incoming == False:
            edges = self.__nodes.get(node,None)
            if edges != None:
                for e in edges:
                    w = self.__nodes[node][e]
                    ret.append((node, e, w))
                return ret
        else:
            for n in self.__nodes:
                edge = self.__nodes[n].get(node,None)
                if edge != None:
                    ret.append((n,node, edge))
            return ret
         
    def edges(self):
        """Returns all the edges in a list of triplets"""
        ret = []
        for node in self.__nodes:
            for edge in self.__nodes[node]:
                w = self.__nodes[node][edge]
                ret.append((node,edge, w))
        return ret
 
    def edgeIn(self,node1,node2):
        """Checks if edge node1 --> node2 is present"""
        n1 = self.__nodes.get(node1, None)
        if n1 != None:
            n2 = self.__nodes[node1].get(node2, None)
            if n2 != None:
                return True
            else:
                return False
        else: 
            return False 

class DiGraphLLAnalyzer(DiGraphLL):
    
    def Dijkstra(self,root):
        """
        returns a dictionary with all the distances
        node by node and a previous structure
        to go from one node to the root through the
        shortest path
        """
        
        def findNodeWithMinWeight(dist,nodes):
            """
            helper function to find the node
            with minimum weight among a set
            """

            minNode = nodes[0]
            minWeight = dist[minNode]

            for node in nodes:
                w = dist.get(node, math.inf)
                if w < minWeight:
                    minWeight = w
                    minNode = node
            return minNode,minWeight
                    
        dist = dict()
        prev = dict()
        for x in self.nodes():
            dist[x] = math.inf
        
        dist[root] = 0
        Q = deque()
        Q.extend(self.nodes())
        #print(Q)
        while len(Q) > 0:
            N,distN = findNodeWithMinWeight(dist,Q)
            
            Q.remove(N)
            #print(Q)
            outgoingEdges = self.adjacentEdge(N, incoming = False)
            #print(outgoingEdges)
            if len(outgoingEdges) > 0:
                for edge in outgoingEdges:
                    #edge is like (n, otherNode, weight)
                    newDist = edge[2] + distN

                    if newDist < dist[edge[1]]:
                        dist[edge[1]] = newDist
                        prev[edge[1]] = edge[0]
            
        return dist,prev
    
                
if __name__ == "__main__":
    G = DiGraphLLAnalyzer()
    for i in range(1,10):
        G.insertNode("Node_" + str(i))
        
    G.insertEdge("Node_1", "Node_2",5)
    G.insertEdge("Node_2", "Node_1",7)
    G.insertEdge("Node_1", "Node_3",11)
    G.insertEdge("Node_1", "Node_5",9)
    G.insertEdge("Node_2", "Node_3",1)
    G.insertEdge("Node_2", "Node_5",2)
    G.insertEdge("Node_3", "Node_4",3)
    G.insertEdge("Node_3", "Node_6",2)
    G.insertEdge("Node_5", "Node_3",2)
    G.insertEdge("Node_5", "Node_5",5)
    G.insertEdge("Node_6", "Node_4",7)
    G.insertEdge("Node_6", "Node_6",4)
    G.insertEdge("Node_7", "Node_5",3)
    G.insertEdge("Node_5", "Node_8",1)
    G.insertEdge("Node_8", "Node_7",12)
    G.insertEdge("Node_9", "Node_2",10)
    
    root = "Node_1"
    D,P = G.Dijkstra(root)
    
    for dist in D:
        if D[dist] != math.inf:
            print("\nDistance {} - {}: {}".format(root, 
                                                dist,
                                                D[dist]))
            prev = P.get(dist,None)
            tmp = dist
            cnt = 0
            while prev != None:
                print("{}{} <-- {}".format("\t"*cnt,tmp,prev))
                tmp = prev
                prev = P.get(prev,None)
                cnt += 1