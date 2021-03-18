# Title         : HashTable(chaining).py
# Description   : HashTable -> chaining 기법
# Link          : https://www.fun-coding.org/Chapter09-hashtable-live.html

hash_table = list([0 for i in range(8)]) # 값 0을 할당

def get_key(data):
    return hash(data) # 해쉬라는 내부 명령어

def hash_function(key):
    return key % 8 # length = 8

def save_data(data, value):
    index_key = get_key(data) # index에 관련된 key를 따로 저장하는 이유 : 링크드 리스트 데이터 구분을 위해서
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key: # 똑같은 index data가 들어왔다면
                hash_table[hash_address][index][1] = value # 그 값을 수정하여 데이터 새로 삽입
                return
        hash_table[hash_address].append([index_key, value]) # 아닐 시 새로운 데이터 새롭게 삽입
    else:
        hash_table[hash_address] = [[index_key, value]] # 일반적인 경우 dictionary처럼 hash table에 저장

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None
