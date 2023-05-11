class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        self.head = ListNode(value)
        
    
    def append(self, value):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        new_node = ListNode(value)
        current_node.next = new_node
        self.length += 1
    

    def printList(self):
        current_node = self.head
        print(f"{current_node.value} ->", end=" ")

        while current_node.next is not None:
            current_node = current_node.next
            print(f"{current_node.value} ->", end=" ")




