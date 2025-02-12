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
        return hash(key)%self.size
        
    def insert_value(self,key):
        index = self.hash_key(key)
        
        while self.table[index] is not None:
            index = (index+1)%self.size
        self.table[index] = key
        
    def delete(self,key):
        index = self.hash_key(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = None
                print(f"Deleted key {key} at index {index}")
                return
            index = (index+1)%self.size
        
    def print_table(self):
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")
def main():
    prob = TombStone(5)
    prob.insert_value(3)
    prob.insert_value(5)
    prob.insert_value(5)
    prob.insert_value(5)
    prob.insert_value(2)
    prob.delete(3)
    prob.delete(5)
    prob.delete(5)
    prob.delete(5)
    prob.insert_value(3)
    prob.insert_value(17)
    prob.insert_value(13)
    prob.insert_value(11)
    prob.delete(11)
    
    prob.delete(2)
    prob.print_table()
        
if __name__ == "__main__":
        main()