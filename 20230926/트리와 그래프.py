from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node(value={self.data}, left={self.left}, right={self.right})"

    def __repr__(self):
        return f"Node(value={self.data}, left={self.left}, right={self.right})"


class Tree:
    def __init__(self, root: Any):
        self.root = Node(root)
        self.__count = 1

    def add(self, data: Any):
        current: Node = self.root
        prev: Node = None
        new_node = Node(data)
        while current:
            prev = current
            if data > current.data:  # 데이터가 current.data보다 크면 오른쪽 Node 불러오기
                current = current.right
            elif data < current.data:  # 데이터가 current.data보다 크면 왼쪽 Node 불러오기
                current = current.left
            else:  # 데이터가 존재하는경우 리턴
                return

        if data > prev.data:
            prev.right = new_node
        else:
            prev.left = new_node
        self.__count += 1

    # 깊이 우선 (Stack)
    def DFS(self):
        result = []
        stack = [self.root]

        while stack:
            current = stack.pop()
            result.append(current)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    # 너비 우선 (Queue)
    def BFS(self):
        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)

    def __len__(self):
        return self.__count

    def __str__(self):
        return f"Tree(root={self.root})"

    def __repr__(self):
        return f"Tree(root={self.root})"


tree = Tree("A")
tree.add("B")
tree.add("C")
tree.add("D")
tree.add("E")
tree.add("F")
tree.add("G")

print(tree)
print(len(tree))
