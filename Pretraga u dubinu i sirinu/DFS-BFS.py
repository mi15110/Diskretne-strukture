#!/usr/bin/env python
# coding: utf-8

# # Implementacija algoritama za obilazak grafa u dubinu i širinu

# In[5]:


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
  
    # DFS rekurzivni obilazak grafa
    def DFS(self, a): 
        # Obeležava se da je čvor posećen i štampa se
        a.visited = True
        print("Posećen čvor -> ", a.value) 
  
        # Rekurzivno se obilaze deca čvora a koja nisu posećena
        for i in self.graph[a]: 
            if i.visited == False: 
                self.DFS(i)
                
    # BFS obilazak grada
    def BFS(self, a): 
        
        # Roditelj se dodaje u red i obeležava se da je posećen
        queue = [] 
        queue.append(a) 
        s.visited = True
        
        # Sve dok postoji čvorova u redu čvor a se skida iz reda i obilaze se njegova deca
        while queue: 
  
            a = queue.pop(0) 
            print("Posećen čvor -> ", a.value) 
            
            for i in self.graph[a]: 
                if i.visited == False: 
                    queue.append(i) 
                    i.visited = True
        
    # Resetovanje posećenosti čvorova
    def unvisited(self):
        for graphs in self.graph: 
            graphs.visited = False
                
def main():

    # Kreiranje grafa
    g = Graph()

    # Kreiranje čvorova grafa
    a0  = Node("a0")
    a1  = Node("a1")
    a2  = Node("a2")
    a3  = Node("a3")
    a4  = Node("a4")

    
    
    g.addEdge(a0, a1) 
    g.addEdge(a0, a2) 
    g.addEdge(a1, a2) 
    g.addEdge(a2, a0) 
    g.addEdge(a2, a3) 
    g.addEdge(a3, a3) 
    g.addEdge(a3, a4)
  
    
    
    print("Primena algoritma obilaska grafa u dubinu: ")
    g.DFS(a2)
    
    g.unvisited()
    
    print("\n")
    print("Primena algoritma obilaska grafa u širinu: ")
    g.BFS(a2)
    

if __name__ == "__main__":
    main()

