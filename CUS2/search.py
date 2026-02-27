import sys
from parser import parse_file
from weightedastar import weighted_astar

def main():
    filename = sys.argv[1]
    method = sys.argv[2]

    edges, origin, destinations, nodes = parse_file(filename)

    if filename is None:
        print("No file provided")
        exit()

    if method == "CUS2":
        number_of_nodes, path = weighted_astar([origin], [destinations[0]], edges, nodes)
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