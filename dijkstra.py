# ============================================================
#          DIJKSTRA'S SHORTEST PATH FINDER
#          Mathematics Activity - Python Console Program
#          Directed Weighted Graph
# ============================================================

import heapq


# ------------------------------------------------------------
# Function to add an edge
# ------------------------------------------------------------
def add_edge(graph, source, destination, weight):

    if source not in graph:
        graph[source] = []

    if destination not in graph:
        graph[destination] = []

    # Directed edge: source -> destination
    graph[source].append((destination, weight))


# ------------------------------------------------------------
# Function to display the graph
# ------------------------------------------------------------
def display_graph(graph):

    print("\n" + "=" * 60)
    print("                    GRAPH")
    print("=" * 60)

    if not graph:
        print("Graph is empty.")
        return

    print("Graph Type: DIRECTED WEIGHTED GRAPH")
    print("-" * 60)

    for vertex in graph:

        print(f"{vertex} -> ", end="")

        if len(graph[vertex]) == 0:
            print("No outgoing edges")
            continue

        connections = []

        for neighbour, weight in graph[vertex]:

            connections.append(
                f"{neighbour} ({weight})"
            )

        print(", ".join(connections))


# ------------------------------------------------------------
# Dijkstra's Algorithm
# ------------------------------------------------------------
def dijkstra(graph, source):

    # Store shortest distance of each vertex
    distances = {}

    # Store previous vertex for shortest path
    previous = {}

    # Initially all distances are infinity
    for vertex in graph:

        distances[vertex] = float("inf")
        previous[vertex] = None

    # Distance from source to itself is 0
    distances[source] = 0

    # Priority queue
    priority_queue = [(0, source)]

    print("\n" + "=" * 60)
    print("              DIJKSTRA'S ALGORITHM")
    print("=" * 60)

    step = 1

    while priority_queue:

        # Select vertex with minimum distance
        current_distance, current_vertex = heapq.heappop(
            priority_queue
        )

        # Ignore outdated distance
        if current_distance > distances[current_vertex]:
            continue

        print(f"\nStep {step}")
        print("-" * 50)

        print(
            f"Selected vertex: {current_vertex}"
        )

        print(
            f"Current distance: {current_distance}"
        )

        # Check all outgoing edges
        for neighbour, weight in graph[current_vertex]:

            new_distance = (
                current_distance + weight
            )

            print(
                f"\nChecking edge: "
                f"{current_vertex} -> {neighbour}"
            )

            print(
                f"Calculation: "
                f"{current_distance} + {weight} "
                f"= {new_distance}"
            )

            # Update if shorter distance is found
            if new_distance < distances[neighbour]:

                distances[neighbour] = new_distance

                previous[neighbour] = current_vertex

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbour)
                )

                print(
                    f"Updated distance of "
                    f"{neighbour}: {new_distance}"
                )

            else:

                print(
                    f"No update required."
                )

        step += 1

    return distances, previous


# ------------------------------------------------------------
# Function to reconstruct shortest path
# ------------------------------------------------------------
def get_shortest_path(
        previous,
        source,
        destination):

    path = []

    current = destination

    while current is not None:

        path.append(current)

        current = previous[current]

    # Reverse the path
    path.reverse()

    # Destination cannot be reached
    if len(path) == 0 or path[0] != source:

        return []

    return path


# ------------------------------------------------------------
# Function to enter graph
# ------------------------------------------------------------
def enter_graph():

    graph = {}

    print("\n" + "=" * 60)
    print("              ENTER DIRECTED GRAPH")
    print("=" * 60)

    # Number of vertices
    while True:

        try:

            number_of_vertices = int(
                input(
                    "\nEnter number of vertices: "
                )
            )

            if number_of_vertices <= 0:

                print(
                    "Number of vertices must be "
                    "greater than 0."
                )

                continue

            break

        except ValueError:

            print(
                "Please enter a valid integer."
            )

    # Number of edges
    while True:

        try:

            number_of_edges = int(
                input(
                    "Enter number of edges: "
                )
            )

            if number_of_edges < 0:

                print(
                    "Number of edges cannot be negative."
                )

                continue

            break

        except ValueError:

            print(
                "Please enter a valid integer."
            )

    # --------------------------------------------------------
    # Enter vertices
    # --------------------------------------------------------

    print("\nEnter the vertices.")

    for i in range(number_of_vertices):

        while True:

            vertex = input(
                f"Enter vertex {i + 1}: "
            ).strip()

            if vertex == "":

                print(
                    "Vertex cannot be empty."
                )

            elif vertex in graph:

                print(
                    "This vertex already exists."
                )

            else:

                graph[vertex] = []

                break

    # --------------------------------------------------------
    # Enter directed edges
    # --------------------------------------------------------

    print("\nEnter the directed edges.")

    print(
        "Format: Source Destination Weight"
    )

    print(
        "Example: A B 4 means A -> B with weight 4"
    )

    print(
        "Note: Negative weights are not allowed."
    )

    for i in range(number_of_edges):

        print(f"\nEdge {i + 1}")

        while True:

            data = input(
                "Enter source, destination and weight: "
            ).split()

            # Check input format
            if len(data) != 3:

                print(
                    "\nInvalid format!"
                )

                print(
                    "Example: A B 4"
                )

                continue

            source = data[0]

            destination = data[1]

            # Check source vertex
            if source not in graph:

                print(
                    f"Vertex '{source}' "
                    f"does not exist."
                )

                continue

            # Check destination vertex
            if destination not in graph:

                print(
                    f"Vertex '{destination}' "
                    f"does not exist."
                )

                continue

            # Convert weight to number
            try:

                weight = float(data[2])

            except ValueError:

                print(
                    "Weight must be a number."
                )

                continue

            # Dijkstra does not support negative weights
            if weight < 0:

                print(
                    "Negative weights are not allowed "
                    "in Dijkstra's Algorithm."
                )

                continue

            # Add directed edge
            add_edge(
                graph,
                source,
                destination,
                weight
            )

            break

    print("\nGraph successfully created!")

    return graph


# ------------------------------------------------------------
# Function to find shortest path
# ------------------------------------------------------------
def find_shortest_path(graph):

    if not graph:

        print(
            "\nPlease enter a graph first."
        )

        return

    print("\n" + "=" * 60)
    print("              FIND SHORTEST PATH")
    print("=" * 60)

    source = input(
        "Enter source vertex: "
    ).strip()

    destination = input(
        "Enter destination vertex: "
    ).strip()

    # Check source
    if source not in graph:

        print(
            "\nSource vertex does not exist."
        )

        return

    # Check destination
    if destination not in graph:

        print(
            "\nDestination vertex does not exist."
        )

        return

    # Run Dijkstra
    distances, previous = dijkstra(
        graph,
        source
    )

    # Find shortest path
    path = get_shortest_path(
        previous,
        source,
        destination
    )

    # Display result
    print("\n" + "=" * 60)
    print("                    RESULT")
    print("=" * 60)

    if not path:

        print(
            f"\nNo path exists from "
            f"{source} to {destination}."
        )

    else:

        print("\nShortest Path:")

        print(
            " -> ".join(path)
        )

        print(
            f"\nMinimum Distance: "
            f"{distances[destination]}"
        )


# ------------------------------------------------------------
# Function to display all shortest distances
# ------------------------------------------------------------
def display_all_distances(graph):

    if not graph:

        print(
            "\nPlease enter a graph first."
        )

        return

    source = input(
        "\nEnter source vertex: "
    ).strip()

    if source not in graph:

        print(
            "\nVertex does not exist."
        )

        return

    # Run Dijkstra
    distances, previous = dijkstra(
        graph,
        source
    )

    print("\n" + "=" * 60)
    print(
        f"      SHORTEST DISTANCES FROM {source}"
    )
    print("=" * 60)

    for vertex in graph:

        if distances[vertex] == float("inf"):

            print(
                f"{source} -> {vertex} = No path"
            )

        else:

            print(
                f"{source} -> {vertex} = "
                f"{distances[vertex]}"
            )


# ------------------------------------------------------------
# Main Menu
# ------------------------------------------------------------
def main():

    graph = {}

    while True:

        print("\n")

        print("=" * 60)
        print("       DIJKSTRA'S SHORTEST PATH FINDER")
        print("=" * 60)

        print("Graph Type: Directed Weighted Graph")

        print("\n1. Enter Graph")
        print("2. Display Graph")
        print("3. Find Shortest Path")
        print("4. Display All Shortest Distances")
        print("5. Exit")

        print("-" * 60)

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # Enter graph
        # ----------------------------------------------------

        if choice == "1":

            graph = enter_graph()

        # ----------------------------------------------------
        # Display graph
        # ----------------------------------------------------

        elif choice == "2":

            display_graph(graph)

        # ----------------------------------------------------
        # Find shortest path
        # ----------------------------------------------------

        elif choice == "3":

            find_shortest_path(graph)

        # ----------------------------------------------------
        # Display all distances
        # ----------------------------------------------------

        elif choice == "4":

            display_all_distances(graph)

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif choice == "5":

            print("\n" + "=" * 60)

            print(
                "Thank you for using "
                "Dijkstra's Shortest Path Finder!"
            )

            print(
                "Program terminated successfully."
            )

            print("=" * 60)

            break

        # ----------------------------------------------------
        # Invalid choice
        # ----------------------------------------------------

        else:

            print(
                "\nInvalid choice!"
            )

            print(
                "Please enter a number from 1 to 5."
            )


# ------------------------------------------------------------
# Start the program
# ------------------------------------------------------------

if __name__ == "__main__":

    main()
