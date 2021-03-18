# Title         : BST.py
# Description   : Binary Search Tree -> Tree Linked List를 활용
# Link          : https://www.fun-coding.org/Chapter10-bst.html

# BST 활용 예제 : 임의로 중복안되는 100개 추출
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        self.current_node = self.root
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None: # 값이 왼쪽에 없는 경우
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None: # 값이 오른쪽에 없는 경우
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    
    # BST 검색 알고리즘
    def search(self, value):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    # BST 삭제 알고리즘
    def delete(self, value):
        # 삭제할 node가 있는지 파악
        searched = False
        self.current_node = self.root
        self.parent = self.root
        while self.current_node: # 현재 node값이 존재하는 경우 시작
            if self.current_node.value == value: # 찾는 값이 존재하는 경우
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        
        if searched == False:
            return False
        
        ### case 1 : Leaf node 삭제
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node # 메모리 상에서 삭제

        ### case 2 : chile node를 한 개 가지고 있을 때, 왼쪽 오른쪽 구분해서 삭제
        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        ### case 3 : child node를 두 개 가지고 있을 때
        elif self.current_node.left != None and self.current_node.right != None:
            
            # case 3-1 : 삭제할 node가 왼쪽에 있을 때, 가장 큰 값을 올려주기
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left

            # case 3-2 : 삭제할 node가 오른쪽에 있을 때, 가장 작은 값을 올려주기
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.right
        return True

bst_nums = set()
while len(bst_nums)!=100:
    bst_nums.add(random.randint(0,999))

# 500 root node로 설정
root = Node(500)
BT = BST(root)
for num in bst_nums:
    BT.insert(num)

# BST search
for num in bst_nums:
    if BT.search(num) == False:
        print("Fail")

# BST delete
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

for del_num in delete_nums:
    if BT.delete(del_num) == False:
        print('Fail')