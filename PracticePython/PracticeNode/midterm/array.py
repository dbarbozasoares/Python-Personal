class Node:
    
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoublyLinkedList:           
    def __init__(self):
        self.front = None
        self.back = None
        
    def push_front(self, data):
        nn = Node(data, self.front)
        if self.front is None:
            self.back = nn
        else:
            self.front.prev = nn
        
        self.front = nn 

    def remove_descreasing(self):
        curr =  self.front
        while curr:
            if curr.prev:
                if curr.data < curr.prev.data:
                    if curr == self.back and curr.prev == self.front:
                        self.back = self.front
                        self.front = self.back
                        self.back.next = None
                        self.front.prev = None
                    elif curr.prev == self.front:
                        self.front.next = curr.next
                        curr.next.prev = self.front
                    elif curr == self.back:
                        self.back.prev.next = None
                        self.back = curr.prev
                        
                    else:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
            curr = curr.next
        return True        
    def print_list(self):
        current = self.front
        while current != self.back.next:
            print(current.data, end=" <--> ")    
            current = current.next
        print("END")
        
i = 0 #GLOBAL
def is_desc(array):
    global i
    print(i)
    if i == (len(array)-1):
        i = 0
        return True
    if is_greater(array[i], array[i+1]) == False:
        i = 0
        return False
    i += 1
    return is_desc(array)
        
def find_pair(array, target):
    res = {}
    for key in range(len(array)):
        a = target - array[key]
        if a in res:
            return [res[a],key] 
        res[array[key]] = key
def is_greater(a,b):
    return a > b
    
def main():
    # myArr = DoublyLinkedList()
    # myArr.push_front(19)
    # myArr.push_front(18)
    # myArr.push_front(15)
    # myArr.push_front(12)
    # myArr.push_front(17)
    # myArr.push_front(16)
    # myArr.print_list()
    # myArr.remove_descreasing()
    # myArr.print_list()
    arr = [5,3,2,1]
    arr2 = [2,1,3,5]
    print(is_desc(arr))
    print(is_desc(arr2))
    print(find_pair(arr,3))
if __name__ == "__main__":
    main()