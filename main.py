# total graph

import heapq

class Graph():
    def __init__(self):
      self.buildingMap = {}
      
    def add_vertex(self, vertex):
      if vertex not in self.buildingMap:
        self.buildingMap[vertex] = []
        
    def add_edge(self, vertex1, vertex2, weight):
      if vertex1 not in self.buildingMap:
        self.add_vertex(vertex1)
        
      if vertex2 not in self.buildingMap:
        self.add_vertex(vertex2)
        
      self.buildingMap[vertex1].append((vertex2,weight))
      # self.buildingMap[vertex2].append((vertex1,weight))
        
    def get_vertices(self):
      return list(self.buildingMap.keys())
    
    def get_edges(self, vertex):
      return self.buildingMap[vertex]
    
    def dijkstra(self, start):
        # Initialize distances to all vertices as infinity except the starting vertex, which has distance 0
        distances = {v: float('inf') for v in self.get_vertices()}
        distances[start] = 0
        
        # Initialize the heap queue with the starting vertex and its distance
        pq = [(0, start)]
        
        while pq:
            # Get the vertex with the smallest distance from the heap queue
            curr_dist, curr_vert = heapq.heappop(pq)
            
            # If the distance to this vertex is already smaller than the distance in the heap queue, skip it
            if curr_dist > distances[curr_vert]:
                continue
            
            # For each adjacent vertex, update its distance if a shorter path is found
            for neighbor, weight in self.get_edges(curr_vert):
                distance = distances[curr_vert] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances
      
    def bellman_ford(self, start):
          # Initialize distances to all vertices as infinity except the starting vertex, which has distance 0
          distances = {v: float('inf') for v in self.get_vertices()}
          distances[start] = 0
          
          # Relax edges V-1 times
          for _ in range(len(self.get_vertices()) - 1):
              for v in self.get_vertices():
                  for neighbor, weight in self.get_edges(v):
                      if distances[v] != float('inf') and distances[v] + weight < distances[neighbor]:
                          distances[neighbor] = distances[v] + weight
          
          # Check for negative cycles
          for v in self.get_vertices():
              for neighbor, weight in self.get_edges(v):
                  if distances[v] != float('inf') and distances[v] + weight < distances[neighbor]:
                      raise ValueError("Negative cycle detected")
          
          return distances
       

def addVertices():
  global graph
  #list of all vertices
  allVertices = ["College Square", "Lewis Science Center", "Speech Language Hearing", "Computer Science",
                "Burdick", "Prince Center","Torreyson Library","Maintenance College","Old Main",
                "Police Dept","Fine Art","McALister Hall","Student Center","Wingo",
                "Student Health Center","New Business Building","Oak Tree Apt","Brewer-Hegeman",
                "Bear Village Apt"]
  # adding all the vertex in graph
  for vertex in allVertices:
    graph.add_vertex(vertex)
 
  
def addEdges():
  global graph
  graph.add_edge("Maintenance College","Speech Language Hearing",120)
  graph.add_edge("Maintenance College","Burdick",300)
  graph.add_edge("Maintenance College","McALister Hall",150)
  graph.add_edge("Maintenance College","Wingo",100)
  graph.add_edge("Maintenance College","New Business Building",150)
  graph.add_edge("Maintenance College","Oak Tree Apt",160)
  graph.add_edge("Oak Tree Apt","Maintenance College",160)
  graph.add_edge("Oak Tree Apt","Brewer-Hegeman",40)
  graph.add_edge("Oak Tree Apt","New Business Building",30)
  graph.add_edge("Speech Language Hearing","Lewis Science Center",250)
  graph.add_edge("Speech Language Hearing","Burdick",100)
  graph.add_edge("Speech Language Hearing","Maintenance College",120)
  graph.add_edge("Bear Village Apt","Brewer-Hegeman",350)
  graph.add_edge("Brewer-Hegeman","New Business Building",20)
  graph.add_edge("Brewer-Hegeman","Student Health Center",200)
  graph.add_edge("Brewer-Hegeman","Bear Village Apt",350)
  graph.add_edge("Brewer-Hegeman","Oak Tree Apt",40)
  graph.add_edge("New Business Building","Wingo", 50)
  graph.add_edge("New Business Building","Student Center", 110)
  graph.add_edge("New Business Building","Brewer-Hegeman", 20)
  graph.add_edge("New Business Building","Maintenance College", 150)
  graph.add_edge("New Business Building","Oak Tree Apt", 30)
  graph.add_edge("Wingo","McALister Hall",50)
  graph.add_edge("Wingo","Student Center",100)
  graph.add_edge("Wingo","New Business Building",50)
  graph.add_edge("Wingo","Maintenance College",100)
  graph.add_edge("McALister Hall","Burdick",200)
  graph.add_edge("McALister Hall","Old Main",100)
  graph.add_edge("McALister Hall","Fine Art",180)
  graph.add_edge("McALister Hall","Student Center",100)
  graph.add_edge("McALister Hall","Wingo",50)
  graph.add_edge("McALister Hall","Maintenance College",150)
  graph.add_edge("Burdick","Speech Language Hearing", 100)
  graph.add_edge("Burdick","Computer Science", 30)
  graph.add_edge("Burdick","Torreyson Library", 80)
  graph.add_edge("Burdick","McALister Hall", 200)
  graph.add_edge("Burdick","Maintenance College", 300)
  graph.add_edge("Student Center","Fine Art", 80)
  graph.add_edge("Student Center","Student Health Center", 50)
  graph.add_edge("Student Center","New Business Building", 110)
  graph.add_edge("Student Center","Wingo", 100)
  graph.add_edge("Student Center","McALister Hall", 100)
  graph.add_edge("Fine Art","Old Main", 90)
  graph.add_edge("Fine Art","Police Dept", 50)
  graph.add_edge("Fine Art","Student Center", 80)
  graph.add_edge("Fine Art","McALister Hall", 180)
  graph.add_edge("Old Main","Torreyson Library", 30)
  graph.add_edge("Old Main","Police Dept", 200)
  graph.add_edge("Old Main","Fine Art", 90)
  graph.add_edge("Old Main","McALister Hall", 100)  
  graph.add_edge("Torreyson Library","Computer Science", 40)
  graph.add_edge("Torreyson Library","Prince Center", 30)
  graph.add_edge("Torreyson Library","Old Main", 30)
  graph.add_edge("Torreyson Library","Burdick", 80)
  graph.add_edge("Computer Science","Lewis Science Center", 150)
  graph.add_edge("Computer Science","Prince Center", 80)
  graph.add_edge("Computer Science","Torreyson Library", 40)
  graph.add_edge("Computer Science","Burdick", 30)
  graph.add_edge("Lewis Science Center","College Square",200);
  graph.add_edge("Lewis Science Center","Computer Science",150);
  graph.add_edge("Lewis Science Center","Speech Language Hearing",250);
  graph.add_edge("College Square","Lewis Science Center",200)
  graph.add_edge("College Square","Prince Center",300)
  graph.add_edge("Prince Center","College Square", 300)
  graph.add_edge("Prince Center","Police Dept", 100)
  graph.add_edge("Prince Center","Torreyson Library", 30)
  graph.add_edge("Prince Center","Computer Science", 80)
  graph.add_edge("Police Dept","Prince Center",100);
  graph.add_edge("Police Dept","Student Health Center",100);
  graph.add_edge("Police Dept","Old Main",200);
  graph.add_edge("Police Dept","Fine Art",50);
  graph.add_edge("Student Health Center","Police Dept",100);
  graph.add_edge("Student Health Center","Student Center",50);
  graph.add_edge("Student Health Center","Brewer-Hegeman",200);


def main():
  
  global graph
  addVertices();
  addEdges();
  
  
  print("****************************************************")
  print("Implementing Dijkstra Algorithm")
  print("****************************************************")
  distance=graph.dijkstra("Computer Science")
  for key in distance.keys():
    print(f"{key} ------- {distance[key]}"); 
    
    
    
  print("***************************************************\n")
  
  print("Implementing Bellman-Ford Algorithm")
  print("*****************************************************")
  distance=graph.bellman_ford("Computer Science");
  for key in distance.keys():
    print(f"{key} ------- {distance[key]}");
  print("*****************************************************")
  
graph = Graph();
main()
























