import sys

def dfs_search(graph, origin, destinations):
    """
    Performs Depth-First Search to find a path from origin to a destination.
    """
    # Stack stores tuples of: (current_node, path_so_far)
    frontier = [(origin, [origin])]
    explored = set()
    
    # Initialize node counter (starting with 1 for the origin node)
    nodes_created = 1 

    while frontier:
        # LIFO: Pop the last element added to the stack
        current_node, path = frontier.pop()

        # 1. Goal Check
        if current_node in destinations:
            return current_node, nodes_created, path

        # 2. Mark as explored
        if current_node not in explored:
            explored.add(current_node)

            # 3. Get neighbors (avoiding nodes we've already fully explored)
            neighbors = graph.get(current_node, [])
            unvisited_neighbors = [n for n in neighbors if n not in explored]

            # 4. Tie-breaking rule [cite: 83-84]
            # To expand in ascending order, the smallest node needs to be on TOP of the stack.
            # Therefore, we sort neighbors in DESCENDING order before pushing.
            unvisited_neighbors.sort(reverse=True)

            # 5. Push to frontier
            for neighbor in unvisited_neighbors:
                frontier.append((neighbor, path + [neighbor]))
                nodes_created += 1

    return None, nodes_created, []

# --- Test Data based on the Assignment Graph ---
# Representing the edges as an adjacency list [cite: 49-64]
graph = {
    1: [3, 4],
    2: [1, 3],
    3: [1, 2, 5, 6],
    4: [1, 3, 5],
    5: [3, 4],
    6: [3]
}

origin_node = 2 [cite: 65, 66]
destination_nodes = [4, 5] [cite: 67, 68]

# --- Execution ---
if __name__ == "__main__":
    goal_reached, total_nodes, final_path = dfs_search(graph, origin_node, destination_nodes)
    
    if goal_reached:
        # Format the path as a string separated by dashes
        path_str = "-".join(map(str, final_path))
        
        # Standard output format required by the assignment 
        print("test_graph.txt dfs")
        print(f"{goal_reached} {total_nodes}")
        print(path_str)
    else:
        print("No path found.")