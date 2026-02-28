import sys
from parser import parse_file
from dfs import dfs_search
from bfs import bfs 
from gbfs import gbfs
from astar import astar
from ucs import ucs
from weightedastar import weighted_astar

def main():
    filename = sys.argv[1]
    method = sys.argv[2].upper()
    visualize = len(sys.argv) > 3 and sys.argv[3].lower() == "visualize"

    nodes, edges, costs, origin, destinations = parse_file(filename)

    if filename is None:
        print("No file provided")
        exit()

    if method == "DFS":
        goal, number_of_nodes, path, expanded = dfs_search(edges, origin, destinations)
    elif method == "BFS":
        number_of_nodes, path, expanded = bfs(origin, destinations, edges)
    elif method == "GBFS":  
        number_of_nodes, path, expanded = gbfs(origin, destinations, edges, nodes)
    elif method == "AS":
        number_of_nodes, path, expanded = astar(origin, destinations, edges, costs, nodes)
    elif method == "CUS1":
        number_of_nodes, path, expanded = ucs(origin, destinations, edges, costs, nodes)
    elif method == "CUS2":
        number_of_nodes, path, expanded = weighted_astar(origin, destinations, edges, costs, nodes)
    else:
        print("No method implemented")
        exit()

    if number_of_nodes and path is not None and len(path) > 0:
        print(f"Filename: {filename}, Method: {method}")
        print(f"Goal: {path[-1]}, Number of nodes expanded: {number_of_nodes}") # [-1] to get the last element of the path 
        print(f"Path: {' -> '.join(map(str, path))}")
    else:
        print(filename, method)
        print("Search failed")

    if visualize:
        from visualize import launch
        launch(nodes, edges, origin, destinations, path or [], expanded)

if __name__ == "__main__":
    main()