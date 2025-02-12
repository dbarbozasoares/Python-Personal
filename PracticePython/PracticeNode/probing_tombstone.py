class TombStone():
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.tombstone = "DELETED"
        
        
    def hash_key(self,key):
        return key%self.size
        
    def insert_value(self, key):
        index = self.hash_key(key)
        while self.table[index] is not None and self.table[index] != self.tombstone:
            index = self.hash_key(index+1)
        self.table[index] = key
        
    def print_table(self):
        for item in self.table:
            print(item)
    def delete(self, key):
        index = self.hash_key(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = self.tombstone 
                print(f"Deleted key {key} at index {index}")
                return 
            index = (index + 1) % self.size
         
class ProbingLinear():
    def __init__(self,size):
        self.size = size
        self.table = [None] * size
        
    def hash_key(self, key):
        return key%self.size
        
    def insert_value(self,key):
        index = self.hash_key(key)
        origin_index = index
        
        while self.table[index] is not None:
            index = (index+1)%self.size
            if index is origin_index:
                print("Full list")
                return
        self.table[index] = key
        
    def delete(self,key):
        index = self.hash_key(key)
        origin_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = None
                print(f"Deleted key {key} at index {index}")
                self.rehash(index)
                return
            index = (index+1)%self.size
            if index == origin_index:
                print("Item not found")
                
                
    def rehash(self,deleted_index):
        index = self.hash_key(deleted_index+1)
        while self.table[index] is not None:
            item = self.table[index]
            self.table[index] = None
            self.insert_value(item)
            index = (index+1)%self.size
            
    def print_table(self):
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")
    
def main():
        prob = ProbingLinear(10)
        prob.insert_value(77)
        prob.insert_value(7)
        prob.insert_value(21)
        prob.insert_value(17)
        prob.insert_value(13)
        prob.insert_value(23)
        prob.insert_value(25)
        prob.insert_value(33)
        prob.delete(23)   
        prob.delete(7)
        prob.print_table()
        
if __name__ == "__main__":
        main()