class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
                
    def getRoutes(self,start,end,path=[]):
        if path is None:
            path = []
        path += [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.getRoutes(node,end,path.copy())
                for p in new_paths:
                    paths.append(p)
                    
        return paths    
    
class NumbersPath:
    def __init__(self,graph):
        # self.graph_dict = []
        # for node in graph:
            # for b,value in graph[node].items():
                # if b not in self.graph_dict:
                    # self.graph_dict.append([node,b,value])
        # print(self.graph_dict)
        self.graph_dict = graph
    def getPath(self,start,end,res=[]):
        if res is None:
            res = []
        res += [start]
        
        if start == end:
            return [res]
        # tst = False
        # for n in self.graph_dict:
            # if start == n[0]:
                # tst = True
        # if tst == False:
            # return [start]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in res:
                new_paths = self.getPath(node,end,res.copy())
            for p in new_paths:
                paths.append(p)
        return paths
                
    def shortestPath(self,start,end,path=[],total_weight=0):
        if path is None:
            path = []
        path += [start]
        if start == end:
            return [path.copy(), total_weight]
            
        paths = []
        if start not in self.graph_dict:
            return None
        for node,value in self.graph_dict[start].items():
            if node not in path:
                new_ways = self.shortestPath(node,end,path.copy(), total_weight+value)
            for p in new_ways:
                paths.append(p)
        return paths
                

def main():
    graph = {
    'A': {'B': 2, 'C':3},
    'B': {'E': 4, 'G': 5},
    'C': {'D': 1},
    'D': {'E': 2},
    'E': {'F': 4},
    'F': {'G':1}
    }
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
        ("Toronto", "Paris"),
        ("Toronto","Montreal"),
        ("Dubai","Toronto"),
        ("Montreal","New York")
    ]
    my_graph = NumbersPath(graph)
    
    start = "A"
    end = "G"
    print(my_graph.shortestPath(start,end,[], 0))
if __name__ == "__main__":
    main()
