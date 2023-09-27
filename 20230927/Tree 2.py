from typing import Any


# 자식 노드가 여러개 일경우
class Node:
    def __init__(self, data: Any):
        self.data = data
        self.child: list[Node] | set[Node] = []  # 또는 set {}으로 지정합니다.
        # self.left = None
        # self.right = None
