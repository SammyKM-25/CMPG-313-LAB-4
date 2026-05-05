from collections import deque

# ============================================
# GRAPH DEFINITION - YOUR TREE
# ============================================
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# ============================================
# BFS IMPLEMENTATION
# ============================================
def bfs(graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

# ============================================
# DFS IMPLEMENTATION
# ============================================
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# ============================================
# IDDFS IMPLEMENTATION (FIXED)
# ============================================
def dls(graph, node, depth, visited):
    """Depth Limited Search"""
    visited.append(node)
    if depth <= 0:
        return
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dls(graph, neighbor, depth - 1, visited)

def iddfs(graph, start, max_depth):
    """Iterative Deepening Depth First Search"""
    result = []
    for depth in range(max_depth + 1):
        visited = []
        dls(graph, start, depth, visited)
        # Add new nodes in order they were first visited
        for node in visited:
            if node not in result:
                result.append(node)
    return result

# ============================================
# FUNCTION CALLS
# ============================================
ROOT_NODE = 'A'
MAX_DEPTH = 3

# ============================================
# OUTPUT
# ============================================
print("=" * 60)
print("UNINFORMED SEARCH RESULTS - Lab 4")
print("=" * 60)

print("\nTree Structure:")
print("       A")
print("      / \\")
print("     B   C")
print("    / \\   \\")
print("   D   E   F")
print("        \\")
print("         G")
print(f"\nRoot Node: {ROOT_NODE}")
print(f"Maximum Depth: {MAX_DEPTH}")

print("\n" + "-" * 50)
print("1. BFS (Breadth-First Search)")
print("-" * 50)
bfs_result = bfs(graph, ROOT_NODE)
print(f"Traversal Order: {bfs_result}")

print("\n" + "-" * 50)
print("2. DFS (Depth-First Search)")
print("-" * 50)
dfs_result = dfs(graph, ROOT_NODE)
print(f"Traversal Order: {dfs_result}")

print("\n" + "-" * 50)
print(f"3. IDDFS (Iterative Deepening DFS)")
print(f"   Max Depth Limit = {MAX_DEPTH}")
print("-" * 50)
iddfs_result = iddfs(graph, ROOT_NODE, MAX_DEPTH)
print(f"Traversal Order: {iddfs_result}")

print("\n" + "=" * 60)
print("✓ LAB COMPLETED SUCCESSFULLY")
print("=" * 60)

# Verification
print("\n[VERIFICATION]")
print(f"Total nodes visited in BFS:   {len(bfs_result)} (should be 7)")
print(f"Total nodes visited in DFS:   {len(dfs_result)} (should be 7)")
print(f"Total nodes visited in IDDFS: {len(iddfs_result)} (should be 7)")
print(f"All nodes: {sorted(bfs_result)}")