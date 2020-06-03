#!/usr/bin/env python
# coding: utf-8

# # Implementacija algoritama za obilazak grafa u dubinu i širinu

# In[30]:


from collections import defaultdict 
  
# Klasa koja opisuje čvor grafa    
class Node:
    def __init__(self, a):
        # Inicijalizuje se polje koje čuva podatak da li je čvor posećen
        self.visited = False
        # Inicijalizuje se polje koje čuva podatak o nazivu/vrednosti čvora
        self.value   = a
        
    def __str__(self):
        return "Vrednost čvora: {self.value}\nPosećen: {self.visited}".format(self=self)
    
class Graph: 
  
    def __init__(self): 
        # Inicijalizuje se polje koje će čuvati podatke o grafu
        self.graph = defaultdict(list) 
    
    # Funkcija koja dodaje grafu granu od čvora a do čvora b 
    def addEdge(self, a, b): 
        self.graph[a].append(b) 
  
    # DFS rekurzivni obilazak 
    def DFS(self, a): 
        # Obeležava se da je čvor posećen i štampa se
        a.visited = True
        print("Posećen čvor -> ", a.value) 
  
        # Rekurzivno se obilaze deca čvora a koja nisu posećena
        for i in self.graph[a]: 
            if i.visited == False: 
                self.DFS(i) 

    def BFS(self, s): 
        
        queue = [] 
  
        queue.append(s) 
        s.visited = True
        
        while queue: 
  
            s = queue.pop(0) 
            print("Posećen čvor -> ", s.value) 

            for i in self.graph[s]: 
                if i.visited == False: 
                    queue.append(i) 
                    i.visited = True
        
    def unvisited(self):
        for graphs in self.graph: 
            graphs.visited = False
                
def main():

    # Kreiranje grafa
    g = Graph()

    # Kreiranje čvorova grafa
    a1  = Node("a1")
    a2  = Node("a2")
    a3  = Node("a3")
    a4  = Node("a4")
    a5  = Node("a5")
    a6  = Node("a6")
    a7  = Node("a7")
    a8  = Node("a8")
    a9  = Node("a9")
    a10 = Node("a10")
    a11 = Node("a11")

    # Kreiranje grana
    g.addEdge(a1, a4)
    g.addEdge(a1, a2)
    g.addEdge(a2, a1)
    g.addEdge(a2, a6)
    g.addEdge(a2, a5)
    g.addEdge(a2, a3)
    g.addEdge(a3, a2)
    g.addEdge(a3, a5)
    g.addEdge(a4, a1)
    g.addEdge(a4, a6)
    g.addEdge(a5, a2)
    g.addEdge(a5, a3)
    g.addEdge(a5, a6)
    g.addEdge(a5, a7)
    g.addEdge(a5, a9)
    g.addEdge(a6, a2)
    g.addEdge(a6, a4)
    g.addEdge(a6, a5)
    g.addEdge(a6, a7)
    g.addEdge(a6, a9)
    g.addEdge(a7, a5)
    g.addEdge(a7, a6)
    g.addEdge(a8, a9)
    g.addEdge(a9, a5)
    g.addEdge(a9, a6)
    g.addEdge(a9, a8)
    g.addEdge(a10, a11)
    g.addEdge(a11, a10)
    
    
    print("Primena algoritma obilaska grafa u dubinu: ")
    g.DFS(a6)
    
    g.unvisited()
    
    print("\n")
    print("Primena algoritma obilaska grafa u širinu: ")
    g.BFS(a6)
    

if __name__ == "__main__":
    main()





