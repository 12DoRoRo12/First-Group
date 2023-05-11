# class ListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self, value):
#         self.head = ListNode(value)
        
#     def calculate_last_index(self):
#         last_index = 0
#         current_node = self.head
#         while True:
#             current_node = current_node.next
#             last_index += 1
#             if current_node.next is None:
#                 break
#         return last_index
    
#     def append(self, value):
#         current_node = self.head

#         while current_node.next is not None:
#             current_node = current_node.next

#         new_node = ListNode(value)
#         current_node.next = new_node
    
#     def insert(self, value, index):
#         last_index = self.calculate_last_index()
#         i = 0
#         if index == 0:
#             new_node = self.head
#             self.head = ListNode(value) 
#             self.head.next = new_node
#         elif index > last_index + 1:
#             print("Index Out Of Range Error")
#         elif index == last_index + 1:
#             self.append(value)
#         elif 0 < index < last_index + 1:
#             current_node = self.head
#             while i != index - 1:
#                 current_node = current_node.next
#                 i += 1
#             new_node = ListNode(value)
#             new_node.next = current_node.next
#             current_node.next = new_node
        
        
#     def remove(self, index):
#         last_index = self.calculate_last_index()
#         i = 0
#         if index == 0:
#             self.head = self.head.next 
#         elif index > last_index + 1:
#             print("Index Out Of Range Error")
#         elif index == last_index:
#             current_node = self.head
#             while i != last_index - 1:
#                 current_node = current_node.next
#                 i += 1
#             current_node.next = None
#         elif 0 < index < last_index + 1:
#             current_node = self.head
#             while i != index - 1:
#                 current_node = current_node.next
#                 i += 1
#             delete_item = current_node.next 
#             current_node.next = delete_item.next

#     def printList(self):
#         current_node = self.head
#         print(f"{current_node.value} ->", end=" ")

#         while current_node.next is not None:
#             current_node = current_node.next
#             print(f"{current_node.value} ->", end=" ")


#############################


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        self.head = ListNode(value)
        #ლისთის სიგრძის მთვლელი (1_ია რადგან head node_ს შეიცავს შექმნისას)
        self.length = 1

    # printList ფუნქციის გასამარტივებლად
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        
    
    def append(self, value):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        new_node = ListNode(value)
        current_node.next = new_node
        self.length += 1
    
    def insert(self, value, index):
        #უკანასკნელი ნოდის ინდექსი ლისთის სიგრძეს გამოკლებული 1_ია
        last_index = self.length - 1
        i = 0
        # გვაქვს ოთხი განსხვავებული შემთხვევა: 
        # 1. პირველი ელემენტის დამატება 
        if index == 0:
            new_node = self.head
            self.head = ListNode(value) 
            self.head.next = new_node
            self.length += 1
        # 2.ბოლო ელემენტის დამატება
        elif index == last_index + 1:
            self.append(value)
            self.length += 1
        # 3. შუა ელემენტის დამატება
        elif 0 < index < last_index + 1:
            current_node = self.head
            while i != index - 1:
                current_node = current_node.next
                i += 1
            new_node = ListNode(value)
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
        # 4. არასწორი ინდექსის შეყვანა
        elif index > last_index + 1 or index < 0:
            print("Index Out Of Range Error")
        
        
    def remove(self, index):
        last_index = self.length - 1
        i = 0
         # გვაქვს ოთხი განსხვავებული შემთხვევა: 
        # 1. პირველი ელემენტის წაშლა
        if index == 0:
            self.head = self.head.next 
            self.length -= 1
        # 2.ბოლო ელემენტის წაშლა
        elif index == last_index:
            current_node = self.head
            while i < last_index-1:
                current_node = current_node.next
                i += 1
            current_node.next = None
            self.length -= 1
        # 3. შუა ელემენტის წაშლა
        elif 0 < index < last_index:
            current_node = self.head
            while i != index - 1:
                current_node = current_node.next
                i += 1
            delete_item = current_node.next 
            current_node.next = delete_item.next
            self.length -= 1
        # 4. არასწორი ინდექსის შეყვანა
        elif index > last_index or index < 0:
            print("Index Out Of Range Error")
        
        

    def printList(self):
        for node in self:
            print(f"{node.value} ->", end=" ")
        print()


myList = LinkedList(11)
myList.append(25)
myList.append(-1)
print(myList.length)
myList.printList()

myList.insert(221, 0)
myList.insert(222, 0)
myList.insert(223, 1)
print(myList.length)
myList.printList()

myList.remove(3)
print(myList.length)
myList.printList()

