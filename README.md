# tree_top_view

Given a pointer to the root of a binary tree, print the top view of the binary tree.

The tree as seen from the top the nodes, is called the top view of the tree. For this, the binary tree is visualized as all children have a consistent width and depth from their parent node, for every node. The outside edge nodes determined to be 'top view' nodes will block, like casting a shadow, any interior nodes in the sense of this visualization. It is possible that a shadowed node can be an ancestor to a 'top view' node, depending on a sufficient number of generations of children such that a descendent extends outside of the other existing top view nodes.

## Function Description

Write the `topView` function that takes an input parameter of a root node of a binary tree, and determine the 'top view' nodes from left to right. Print the values, space separated, of these 'top view' nodes in that left to right order.

## Constraints

1 <= Nodes in the tree <= 500
