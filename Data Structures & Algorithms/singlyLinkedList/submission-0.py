class LinkedList:

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head

        for _ in range(index):
            if curr is None:
                return -1
            curr = curr.next

        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        node = self.Node(val)
        node.next = self.head
        self.head = node

    def insertTail(self, val: int) -> None:
        node = self.Node(val)

        if self.head is None:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        curr = self.head

        for _ in range(index - 1):
            if curr.next is None:
                return False
            curr = curr.next

        if curr.next is None:
            return False

        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values