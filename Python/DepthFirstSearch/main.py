from Tree import Node


# DFS Search method
def search(value, node: Node):
    if (node == None):
        return False

    if (node.value == value):
        return True

    return search(value, node.left) or search(value, node.right)


# Sample tree
tree = Node(1,
            Node(2,
                 Node(5, None, None),
                 None),
            Node(7,
                 Node(3, None, None),
                 None)
            )

# Sample input
print(search(7, tree))
print(search(5, tree))
print(search(8, tree))
