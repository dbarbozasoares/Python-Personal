def hash_function(key,table_size):
    return len(key)%table_size
    
def insert_with_chaining(hash_table, key, table_size):
    index = hash_function(key, table_size)
    
    if index not in hash_table:
        hash_table[index] = []
    hash_table[index].append(key)
  
def insert_with_linear_probing(hash_table, key, table_size):
    index = hash_function(key, table_size)
    
    original_index = index
    while index in hash_table:
        index = (index + 1) % table_size  
        if index == original_index: 
            raise Exception("Hash table is full")
    
    hash_table[index] = key    


def main():
    names = ["Mar", "Diego", "Diego", "Jhon", "Paul", "Paula", "Paul", "Maria" ]
    hash_table = {}
    table_size = len(names)
    
    for name in names:
        insert_with_chaining(hash_table,name, table_size)
    
    for index, names_list in hash_table.items():
        print(f"Index {index}: {names_list}")
    
if __name__ == "__main__":
    main()