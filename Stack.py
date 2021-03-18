# Title         : Stack.py
# Description   : push와 pop 직접 구현
# Link          : https://www.fun-coding.org/Chapter06-stack-live.html

# def recursive(data):
#     if data < 0:
#         print('ended')
#     else:
#         print(data)
#         recursive(data - 1)
#         print('returned', data)
# recursive(4)

# stack = list()
# stack.append(5)
# stack.append(3)
# stack.append(7)
# print(stack.pop())

# push와 pop 직접 구현

stack_list = list() # global stack list

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1] # 맨 오른쪽 index
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

print(pop())