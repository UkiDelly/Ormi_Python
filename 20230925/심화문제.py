import copy
from typing import Any


# 노드로 쓸 클래스
class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


# Stack
class Stack:
    def __init__(self, *data: object):
        nodes = [Node(x) for x in data]
        self.__head = nodes[0]

        for i in range(0, len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

    def push(self, item: object):
        node = Node(item)

        current_node: Node = self.__head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def pop(self):
        curr_node: Node = copy.deepcopy(self.__head)
        nodes = [curr_node]
        while curr_node.next is not None:
            curr_node = curr_node.next
            nodes.append(curr_node)

        pop_data = nodes.pop()
        nodes[-1].next = None
        self.__head = nodes[0]
        curr_node = self.__head
        for i in range(0, len(nodes) - 1):
            curr_node.next = nodes[i]
            curr_node = curr_node.next

        return pop_data.data

    def clear(self):
        self.__head = Node(None)

    def __str__(self):
        curr_node: Node = self.__head
        nodes = [str(self.__head)]

        while curr_node.next is not None:
            curr_node = curr_node.next
            nodes.append(str(curr_node))

        return " -> ".join(nodes)

    def __repr__(self) -> str:
        pass


stack = Stack(1, 2, 3, 4)
stack.push(5)
print(stack)
stack.push(6)
print(stack)


val = stack.pop()
print(val)
print(stack)
