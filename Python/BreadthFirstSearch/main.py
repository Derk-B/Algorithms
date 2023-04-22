class Node:
    def __init__(self, value: int, left: 'Node', right: 'Node'):
        self.value = value
        self.left = left
        self.right = right

# BFS


def start(value: int, node: Node) -> bool:
    return search(value, [node])


def search(value: int, queue: list) -> bool:
    if (len(queue) == 0):
        return False

    currentNode, *tail = queue

    if (currentNode.value == value):
        return True

    tail.append(currentNode.left)
    tail.append(currentNode.right)

    return search(value, tail)


# Sample data
node = Node(1, Node(2, Node(3, None, None), None), Node(4, None, None))

# Sample input
print(start(1, node))
print(start(2, node))
print(start(4, node))
