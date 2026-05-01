class Node:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        print(f"index: {index}")
        print(f"self.head:{self.head.val}, self.head.next:{self.head.next.val}")
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            past_head = self.head
            self.head = Node(val)
            self.head.next = past_head
        self.length += 1
        
    def insertTail(self, val: int) -> None:
        if self.tail is None:
            self.tail = Node(val)
            self.head = self.tail
        else:
            new_tail = Node(val)
            self.tail.next = new_tail
            self.tail = self.tail.next
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        before_index = -1
        before_curr = self.head
        curr = self.head
        for i in range(index):
            curr = curr.next
            if before_index >= 0:
                before_curr = before_curr.next
            before_index += 1
        
        if index == self.length-1:
            self.tail = before_curr
            self.tail.next = None
        elif index > 0:
            before_curr.next = curr.next
        else:
            self.head = curr.next

        self.length -= 1
        return True
        
    def getValues(self) -> List[int]:
        val_ls = []
        curr = self.head
        for i in range(self.length):
            val_ls.append(curr.val)
            curr = curr.next

        return val_ls
