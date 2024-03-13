import math
from queue import PriorityQueue

# This is the heuristic function. It's just an example!
# In our case, we assume our nodes lie on a x-y plane, and a closer
# euclidean distance between two nodes indicates a "warmer and warmer" search
def euclidean_distance(node1, node2):
    return math.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)

# This returns the A * path!
def a_star(graph, coordinates, start, goal):
    # Priority queue for the nodes to visit
    open_set = PriorityQueue()
    open_set.put((0, start))
    # Keeps track of the path so far
    came_from = {}

    # Costs from start node to current node (set them all to infinity for now)
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # f_score = g_score + heuristic (set them all to infinity for now)
    f_score = {node: float('inf') for node in graph}
    f_score[start] = euclidean_distance(coordinates[start], coordinates[goal])

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal:
            # We got to the end, so we need to rebuild the path and return it!
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1] # Reverse the path to go from start --> end

        # Otherwise, we need to find the next node in the path
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]

            if tentative_g_score < g_score[neighbor]:
                # This path to neighbor is better than any previous one
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + euclidean_distance(coordinates[neighbor], coordinates[goal])
                open_set.put((f_score[neighbor], neighbor))

    return []  # Return an empty path if there is no path

# Example usage. Use the .txt files to see all the examples
# Copy them into this portion
########## 
graph = {
    '0': {'1': 2, '2': 4},
    '1': {'2': 1, '3': 7, '4': 2},
    '2': {'4': 3},
    '3': {'5': 1},
    '4': {'3': 2, '5': 5, '6': 1},
    '5': {'6': 2},
    '6': {}
}

coordinates = {
    '0': (0, 0),
    '1': (2, 1),
    '2': (4, 0),
    '3': (7, 2),
    '4': (5, 3),
    '5': (8, 3),
    '6': (9, 4)
}
start = '0'
goal = '6'
##########

path = a_star(graph, coordinates, start, goal)
print("Path from", start, "to", goal, ":", path)