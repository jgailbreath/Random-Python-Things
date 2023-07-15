# Binary Tree is a powerful data structure for representing hierarchical relationships, organizing data, and
# performing efficient searching and sorting operations.  A Binary Tree is a hierarchical data structure in
# which each node has at most 2 children, referred to as the left child and right child.  The topmost node is
# called the root.  Each node in the tree can have zero, one, or two children.  If a node has no children, it
# is called a leaf node.  Binary Trees can be either empty (NULL) or non-empty.

# Uses Cases:
#-well suited for representing hierarchichal relationships between elements (in a file system, can represent the
# directory structure)
#-often used in sorting and searching algorithms (Binary Search Tree enables efficient searching, insertion,
# and deletion operations)
#-can be used to evaluate arithmetic expressions (each node represents an operator and the child nodes represent
# the individual operands)

# When To Use:
#-hierarchical relationships or organizing data with a parent-child relationship
#-when efficient searching, insertion, or deletion operations are required
#-when working with pre-sorted data or implementing a sorting algorithm(Ex: Heap Sort, Bianry Heap)
#-when evaluating expressions in mathematicalor programming contexts

# Use cases when you should NOT use a Binary Tree:
#-Large Datasets with Unique identifiers: Generally the primary operation here is going to be
# searching/retrieving elements based on their identifier.  You would want to use a structure that
# could be easily hashed or indexed to allow direct access for faster retrieval times.
#-Balanced Parentheses Checking:  This process is not a relational consideration, but would benefit from
# using a stack (LIFO) to allow easy insertion and deletion to perform comparison.
#-Full Text or Index Searching: