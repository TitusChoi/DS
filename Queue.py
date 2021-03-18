# Title         : Queue.py
# Description   : enqueue와 dequeue 직접 구현
# Link          : https://www.fun-coding.org/Chapter05-queue-live.html

queue_list = list() # global queue list 형태
def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0] # list method에서 가져옴 
    return data

for index in range(10):
    enqueue(index)

enqueue(5)
for index in range(11):
    print(dequeue())