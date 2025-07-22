from collections import deque


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def bfs(root, search):
    if not root:
        return []

    queue = deque([root])

    path: dict[int, list[int]] = {
        root.value: [root.value]
    }

    while queue:
        current = queue.popleft()

        if current.value == search:
            return path[current.value]

        if current.left:
            path[current.left.value] = [current.value, current.left.value] if path.get(
                current.value) is None else path.get(current.value, []) + [current.left.value]

            if current.left.value == search:
                return path[current.left.value]
            queue.append(current.left)

        if current.right:
            path[current.right.value] = [current.value, current.right.value] if path.get(
                current.value) is None else path.get(current.value, []) + [current.right.value]

            if current.right.value == search:
                return path[current.right.value]
            queue.append(current.right)

    return path


root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(bfs(root, 7))
