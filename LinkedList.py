# Title         : LinkedList.py
# Description   : Linked List
# Link          : https://www.fun-coding.org/Chapter07-linkedlist-live.html

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def add(data): # Linked List 추가
    node = head
    while node.next:
        node = node.next
    node.next = Node(data) 

node = Node(1)
head = node
for index in range(2, 10):
    add(index)

# Linked List 부분 추가, 부분 삭제
node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

insert_node = Node(1.5) # Linked List 사이 넣어줄 노드

temp_node = node.next
node.next = insert_node
insert_node.next = temp_node

print(node.data)
while node.next:
    node = node.next
    print(node.data)

# 체계화된 Linked List

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class LL:
    def __init__(self, data):
        self.head = Node(data)
        
    def add(self, data): # 노드 추가 함수
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        
    def output(self): # 출력 함수
        node = self.head
        while node:
            print (node.data)
            node = node.next

    def delete(self, data): # 삭제 함수
        if self.head == '':
            print ("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

linkedlist1 = LL(0)
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.output()