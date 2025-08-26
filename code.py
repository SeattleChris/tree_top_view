from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        current = self.root
        while current.info != val:
            if val < current.info:
                if current.left is None:
                    current.left = Node(val)
                current = current.left
            elif val > current.info:
                if current.right is None:
                    current.right = Node(val)
                current = current.right
        return None

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def topView(root):
    if not root:
        return []
    topNodes = {}  # store the first node at each horizontal distance (hd)
    mn = float('inf')  # Determines min hd to quickly sort later.
    # Using a queue, start BFS with the root node at horizontal distance 0
    q = deque([(root, 0)])
    while q:
        node, hd = q.popleft()
        mn = hd if hd < mn else mn
        if hd not in topNodes:  # store only if this is first time seeing hd
            topNodes[hd] = str(node.info)
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))
    # Extract the nodes from the map in sorted order of their horizontal distances
    # print(' '.join(topNodes[key] for key in sorted(topNodes)))  # O(n * log n) Time and O(n) Space

    # O(n) Time and O(n) Space
    result = [0] * len(topNodes)
    for hd, val in topNodes.items():
        result[hd - mn] = val
    print(' '.join(result))
    return None


tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    tree.create(arr[i])
topView(tree.root)