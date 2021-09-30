graph = {
  '1' : ['4', '2'],
  '2' : ['1', '3', '5', '7', '8'],
  '3' : ['2', '4', '9', '10'],
  '4' : ['1', '3'],
  '5' : ['2', '6', '7'],
  '6' : ['5'],
  '7' : ['2', '5', '8'],
  '8' : ['2', '7'],
  '9' : ['3'],
  '10' : ['3'],
}


visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


dfs(visited, graph, '1')