# Title         : DoublyLinkedList_2.py
# Description   : Doubly Linked List
# Link          : https://www.fun-coding.org/Chapter07-linkedlist-live.html

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev # pointer
        self.data = data
        self.next = next # pointer

class DLL:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def insert_before(self, data, before_data): # before_data 전에 data 집어 넣기
        if self.head == None:
            self.head = Node(data)
            return True            
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.next = node
            return True

    def insert_after(self, data, after_data): # after_data 후에 data 집어 넣기
        if self.head == None:
            self.head = Node(data)
            return True            
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            after_new = node.next
            new.next = after_new
            new.prev = node
            node.next = new
            if new.next == None:
                self.tail = new
            return True

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data) # 새로운 데이터 정의
            node.next = new # 데이터 그 자체
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next

doubly_linked_list = DLL(0)
for data in range(1, 10):
    doubly_linked_list.insert(data)

doubly_linked_list.desc()

doubly_linked_list.insert_before(1.5, 2)
doubly_linked_list.insert(10)
doubly_linked_list.desc()