import sys
from parser import parse_file
from bfs import bfs 

def main():
    filename = sys.argv[1]
    method = sys.argv[2]

    edges, origin, destinations = parse_file(filename)

    if filename is None:
        print("No file provided")
        exit()

    if method == "BFS":
        number_of_nodes, path = bfs(origin, destinations, edges)
    else:
        print("No method implemented")
        exit()

    if number_of_nodes and path is not None:
        print(filename, method)
        print(path[-1], number_of_nodes) # [-1] to get the last element of the path => goal
        print(" ".join(map(str, path)))
    else:
        print(filename, method)
        print("Search failed")

if __name__ == "__main__":
    main()