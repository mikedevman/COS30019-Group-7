import sys
import os

def parse_problem_file(filepath):
    """
    Parses the problem text file based on the assignment specifications.
    """
    nodes = {}
    graph = {}
    origin = None
    destinations = []

    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            
        current_section = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Determine the current section [cite: 70, 72, 75, 76]
            if line.startswith("Nodes:"):
                current_section = "nodes"
                continue
            elif line.startswith("Edges:"):
                current_section = "edges"
                continue
            elif line.startswith("Origin:"):
                current_section = "origin"
                continue
            elif line.startswith("Destinations:"):
                current_section = "destinations"
                continue
                
            # Parse data based on the current section
            if current_section == "nodes":
                # Example: "1: (4,1)" [cite: 71]
                parts = line.split(':')
                node_id = int(parts[0].strip())
                graph[node_id] = [] # Initialize adjacency list for this node
                
            elif current_section == "edges":
                # Example: "(2,1): 4" [cite: 74]
                edge_str, cost_str = line.split(':')
                edge_str = edge_str.strip().strip('()')
                from_node, to_node = map(int, edge_str.split(','))
                cost = int(cost_str.strip())
                
                # Edges are directed as per the assignment [cite: 37, 38]
                if from_node not in graph:
                    graph[from_node] = []
                graph[from_node].append(to_node)
                
            elif current_section == "origin":
                origin = int(line)
                
            elif current_section == "destinations":
                # Example: "5; 4" [cite: 76, 77]
                destinations = [int(x.strip()) for x in line.split(';')]

        return graph, origin, destinations

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error parsing file: {e}")
        sys.exit(1)


def dfs_search(graph, origin, destinations):
    """
    Performs Depth-First Search (DFS)[cite: 85].
    """
    # Stack stores tuples of: (current_node, path_so_far)
    frontier = [(origin, [origin])]
    explored = set()
    
    nodes_created = 1 

    while frontier:
        # LIFO: Pop the last element added to the stack
        current_node, path = frontier.pop()

        # Goal Check [cite: 82]
        if current_node in destinations:
            return current_node, nodes_created, path

        # Mark as explored
        if current_node not in explored:
            explored.add(current_node)

            # Get neighbors (avoiding nodes we've already fully explored)
            neighbors = graph.get(current_node, [])
            unvisited_neighbors = [n for n in neighbors if n not in explored]

            # Tie-breaking rule: expand in ascending order[cite: 83].
            # For DFS (LIFO stack), we sort descending before pushing so the smallest is popped first.
            unvisited_neighbors.sort(reverse=True)

            # Push to frontier
            for neighbor in unvisited_neighbors:
                frontier.append((neighbor, path + [neighbor]))
                nodes_created += 1

    return None, nodes_created, []


def main():
    # 1. Command Line Operation [cite: 90, 93, 97]
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        sys.exit(1)

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    # 2. Parse the input file
    graph, origin, destinations = parse_problem_file(filename)

    # 3. Execute the requested search algorithm
    if method == "DFS":
        goal, nodes_created, path = dfs_search(graph, origin, destinations)
    # You can add elif blocks here for BFS, GBFS, AS, CUS1, CUS2 later [cite: 85]
    else:
        print(f"Error: Method '{method}' is not implemented yet.")
        sys.exit(1)

    # 4. Standard Output Formatting [cite: 98-101]
    if goal is not None:
        path_str = " ".join(map(str, path))
        print(f"{filename} {method}")
        print(f"{goal} {nodes_created}")
        print(path_str)
    else:
        print(f"{filename} {method}")
        print("No path found.")

if __name__ == "__main__":
    main()