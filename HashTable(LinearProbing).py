# Title         : HashTable(LinearProbing).py
# Description   : HashTable -> Linear Probing 기법
# Link          : https://www.fun-coding.org/Chapter09-hashtable-live.html

hash_table = list([0 for i in range(8)]) # 값 0을 할당

def get_key(data):
    return hash(data) 

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data) 
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value] # 비어있는 곳 데이터 삽입하기, 08-2와 다른 것은 데이터 삽입 형태가 빈 곳에 할당하여 삽입한다는 것!
                return
            elif hash_table[index][0] == index_key: # 해당 index 키가 같다면 수정하여 삽입
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0: # Key 값이 저장된 적이 없음
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None