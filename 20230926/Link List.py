from typing import Any


# Node
class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: None | Node = None

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self.data)


# MyList
class MyList:
    def __init__(self, *data: Any) -> None:
        data: list[Node] = [Node(x) for x in data]
        if len(data) == 0:
            self.__head: Node = None
            self.__tail: Node = None
            return
        self.__head: Node = data[0]
        self.__curr: Node = data[0]
        self.__tail: Node = data[-1]

        curr = self.__head
        for i in range(1, len(data)):
            curr.next = data[i]
            curr = curr.next

    def add(self, item: Any) -> None:
        new_node = Node(item)
        self.__tail.next = new_node
        self.__tail = new_node

    def pop(self, index: int | None = None) -> Any:
        tmp = None
        if len(self) == 0 or ((index is not None) and index >= len(self)):
            raise IndexError("인덱스를 초과해서 pop할수 없습니다")

        if index is None:
            tail_index = len(self) - 1
            node = self[tail_index - 1]
            self.__tail = node
            tmp = node.next  # return 값
            node.next = None

        else:
            node = self[index - 1]
            self.__tail = node
            tmp: Node = node.next
            node.next = None
        return tmp

    def insert(self, index: int, item: Any) -> None:
        new_node = Node(item)

        if index == 0:
            new_node.next = self.__head
            self.__head = new_node
            return
        elif index > len(self):
            self.add(item)
            return
        elif index < 0:
            raise IndexError("index is less than 0")

        node = self[index - 1]
        temp = node.next
        node.next, new_node.next = new_node, temp

    def find(self, item: Any):
        curr: Node = self.__head

        for i in range(len(self)):
            if curr.data == item:
                return i
            curr = curr.next
        return -1

    def index(self, item: Any):
        curr: Node = self.__head

        for i in range(len(self)):
            if curr.data == item:
                return i
            curr = curr.next
        raise ValueError("값이 존재 하지 않습니다.")

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __next__(self):
        if self.__curr.next is None:
            raise StopIteration
        tmp = self.__curr
        self.__curr = self.__curr.next
        return tmp

    def __len__(self) -> int:
        count = 0
        curr = self.__head
        while curr:
            curr = curr.next
            count += 1
        return count

    def __getitem__(self, index: int) -> Node:
        curr: Node = self.__head
        for _ in range(index):
            curr = curr.next
        return curr

    def __setitem__(self, index: int, item: Any):
        node = self[index]
        node.data = item

    def __str__(self) -> str:
        l = []
        curr = self.__head
        while curr is not None:
            l.append(str(curr))
            curr = curr.next

        return " -> ".join(l)

    def __repr__(self) -> str:
        l = []
        curr = self.__head
        while curr is not None:
            l.append(str(curr))
            curr = curr.next

        return " -> ".join(l)


m_list = MyList(1, 1, 2, 3, 4, 5)

# for i in MyList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
#     print(i)


c_list = MyList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
c_list.add(11)
print(c_list)
