# Dijkstra-shortest-path

A console-based implementation of **Dijkstra's Shortest Path Algorithm** in Python for a **Discrete Mathematics group activity**.

## 📌 About the Project

This project demonstrates the application of **graph theory** and **shortest path algorithms** using a directed weighted graph.

The program allows the user to:

* Create a directed weighted graph
* Add vertices and directed edges
* Assign weights to edges
* Display the graph
* Find the shortest path between two vertices
* Display the shortest distances from a selected source vertex
* Handle invalid inputs
* Prevent negative edge weights

## 🧠 Algorithm Used

### Dijkstra's Shortest Path Algorithm

Dijkstra's algorithm finds the shortest path from a given source vertex to all other reachable vertices in a weighted graph, provided that all edge weights are non-negative.

The algorithm maintains:

* **Distance:** The current shortest known distance from the source
* **Previous:** The previous vertex in the shortest path
* **Priority Queue:** Used to select the vertex with the minimum current distance

## ⚙️ Features

### 1. Enter Graph

The user can enter:

* Number of vertices
* Number of edges
* Vertex names
* Source vertex
* Destination vertex
* Edge weight

### 2. Display Graph

Displays the graph in the following format:

```text
A -> B (4), C (2)
B -> D (5)
C -> B (1), D (8)
```

### 3. Find Shortest Path

The user can specify a source and destination.

Example:

```text
Shortest Path:
A -> C -> B -> D

Minimum Distance: 8
```

### 4. Display All Shortest Distances

Displays the shortest distance from the selected source to every vertex.

### 5. Input Validation

The program checks for:

* Invalid number of vertices
* Invalid number of edges
* Duplicate vertices
* Empty vertex names
* Non-existent vertices
* Invalid edge format
* Invalid weights
* Negative edge weights

## 🔢 Example

Consider the following directed weighted graph:

```text
A → B (4)
A → C (2)
C → B (1)
B → D (5)
C → D (8)
```

If the source is `A` and destination is `D`, the shortest path is:

```text
A → C → B → D
```

with total distance:

```text
2 + 1 + 5 = 8
```

## ⏱️ Complexity

Using a priority queue implemented with a binary heap:

**Time Complexity:**

```text
O((V + E) log V)
```

**Space Complexity:**

```text
O(V + E)
```

where:

* `V` = Number of vertices
* `E` = Number of edges

## 🛠️ Technologies Used

* Python
* `heapq`
* Graph Theory
* Dijkstra's Shortest Path Algorithm

## ▶️ How to Run

Make sure Python 3 is installed.

Run:

```bash
python dijkstra.py
```

The program will display a menu:

```text
1. Enter Graph
2. Display Graph
3. Find Shortest Path
4. Display All Shortest Distances
5. Exit
```

## 📚 Academic Context

This project was developed as part of a **Discrete Mathematics group activity** to demonstrate the practical application of:

* Graphs
* Directed graphs
* Weighted graphs
* Paths
* Shortest paths
* Dijkstra's Algorithm

## 👥 Group Members

* Member 1 - Mahi Pandey | 24BCE10321
* Member 2 - Janvi Kalra | 24BCE11171
* Member 3 - Rohit Ravindra Jadhav | 24BHI10102
* Member 4 - Vinayak Chaturvedi | 23BAI11151
* Member 5 - Vandit agrawal | 23BCG10035 

## 📄 License

This project is created for educational and academic purposes.
