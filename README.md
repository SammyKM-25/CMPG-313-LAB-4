
---

## Project 3: a-star-route-optimization

```markdown
# A* Search Route Optimisation for Truck Logistics

> Implementation of A* search algorithm to determine optimal delivery routes for truck logistics, comparing performance against BFS, DFS, and IDDFS.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![AI](https://img.shields.io/badge/AI-Search%20Algorithms-red.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

---

## Table of Contents

- [Overview](#overview)
- [The Problem It Solves](#the-problem-it-solves)
- [Key Features](#key-features)
- [Search Algorithms Explained](#search-algorithms-explained)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Author](#author)

---

## Overview

This project implements **A* search algorithm** to determine optimal delivery routes for truck logistics. The algorithm uses heuristic functions (Manhattan and Euclidean distance) to find the shortest path between nodes in a graph. The implementation is compared against BFS (Breadth-First Search), DFS (Depth-First Search), and IDDFS (Iterative Deepening DFS).

The project demonstrates practical application of AI search techniques to logistics and supply chain challenges.

---

## The Problem It Solves

Truck logistics companies face the challenge of:
- **Minimising travel distance** to reduce fuel costs
- **Optimising delivery routes** to save time
- **Maximising efficiency** to improve customer satisfaction
- **Handling complex networks** with multiple delivery points

**The Challenge:** Finding the optimal route in a graph with many nodes and edges. This is a classic problem in AI known as the "shortest path problem."

---

## Key Features

- ✅ **A* Search Algorithm** with custom heuristic functions
- ✅ **Manhattan Distance** heuristic for grid-based routing
- ✅ **Euclidean Distance** heuristic for continuous space
- ✅ **BFS (Breadth-First Search)** – explores level by level
- ✅ **DFS (Depth-First Search)** – explores branch by branch
- ✅ **IDDFS (Iterative Deepening DFS)** – combines DFS with depth limits
- ✅ **Graph Representation** with tree structure (nodes A-G)
- ✅ **Performance Comparison** across all algorithms
- ✅ **Visualisation** of traversal orders

---

## Search Algorithms Explained

### 1. A* Search (A-Star)

**Description:** A* is an informed search algorithm that uses a heuristic function to estimate the cost from the current node to the goal. It combines the advantages of Dijkstra's algorithm and greedy best-first search.

**How it works:**
- f(n) = g(n) + h(n)
- g(n) = cost from start to node n
- h(n) = heuristic estimate from node n to goal

**When to use:** When you have a good heuristic and need the optimal path.

---

### 2. BFS (Breadth-First Search)

**Description:** BFS explores all nodes at the current depth before moving to nodes at the next depth level.

**How it works:**
- Uses a queue (FIFO)
- Visits all neighbors of a node before moving deeper

**When to use:** When looking for the shortest path in an unweighted graph.

---

### 3. DFS (Depth-First Search)

**Description:** DFS explores as far as possible along a branch before backtracking.

**How it works:**
- Uses a stack (LIFO) or recursion
- Visits a node, then recursively visits its children

**When to use:** When memory is limited and you don't need the shortest path.

---

### 4. IDDFS (Iterative Deepening DFS)

**Description:** IDDFS combines DFS with depth limits, increasing the depth limit incrementally until the goal is found.

**How it works:**
- Calls DFS with increasing depth limits (0, 1, 2, ...)
- Completes when all nodes are found

**When to use:** When memory is limited but you need completeness.

---

## Technologies Used

| **Category** | **Technology** | **Version** |
| :--- | :--- | :--- |
| Language | Python | 3.8+ |
| Data Structures | Collections (deque) | - |
| Version Control | Git, GitHub | - |

---

## Installation

### Prerequisites

- Python 3.8 or higher

### Steps

1. **Clone the repository:**

```bash
git clone https://github.com/decodb/a-star-route-optimization.git
cd a-star-route-optimization

2. **Run the script:**

python main.py
