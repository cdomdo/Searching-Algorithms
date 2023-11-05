# Search methods

import search

# Crear una lista de problemas GPS para diferentes pares de ciudades
problems = [search.GPSProblem(start, end, search.romania) 
            for start, end in [('A', 'B'), ('O', 'E'), ('G', 'Z'), ('N', 'D'), ('M', 'F')]]

# Resolver cada problema con diferentes algoritmos y mostrar los resultados
for problem in problems:
    print(f"Problem: {problem.initial} to {problem.goal}")
    
    # Búsqueda en Anchura (Breadth-First Search)
    result = search.breadth_first_graph_search(problem)
    print(f"Breadth-First Path: {result.path()}", "\n")
    
    # Búsqueda en Profundidad (Depth-First Search)
    result = search.depth_first_graph_search(problem)
    print(f"Depth-First Path: {result.path()}", "\n")
    
    # Branch and Bound no subestimation
    result = search.branch_and_bound_graph_search(problem)
    print(f"Branch and Bound Path: {result.path()}", "\n")

    # Branch and Bound with subestimation
    result = search.branch_and_bound_subestimation_graph_search(problem)
    print(f"Branch and Bound with subestimation Path: {result.path()}", "\n")

    print("-" * 50)  # A line to separate each problem's results


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
