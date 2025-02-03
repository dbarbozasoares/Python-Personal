from re import T


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
        self.sort()
        
    def pop_front(self):
        if self.front is not None:
            rm = self.front
            self.front = self.front.next
        if self.front is None:
            self.back = None
        else:
            self.front.prev = None
        del rm
        
    def print_list(self):
        current = self.front
        while current:
            print(current.data, end=" <--> ")
            current = current.next
        print("END")
        
    def sort(self):
        if self.front is None:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.front
            while current and current.next:
                if current.data > current.next.data:
                    temp = current.data
                    current.data = current.next.data
                    current.next.data = temp
                    swapped = True
                current = current.next
    
def find_value(current,value):
    
    index = 0
    if current.next is None:
        return
    while current:
        if current.data == value:
            print("Found at: ", index,"position")
            return index
        current = current.next
        index +=1
    print("Number does not exist in list")
    return -1
def find_max(nod):
    n_max = 0
    node = nod.front
    if node is None:
        return None
    while node:
        n_max = node.data
        if node.data > n_max:
            n_max = node.data
        node = node.next
            
    return n_max

def update_data(node, target, value):
    current = node.front
    if current is None:
        return None
    while current:
        if current.data == target:
            current.data = value
            node.sort()
            return True
        current = current.next
        
    return False
    
def remove_data(node, num):
    if node.front is None:
        return None
    current = node.front
    while current:
        if current.data == num:
            if current == node.front:
                node.front = current.next
                if node.front:
                    node.front.prev = None
                else:
                    node.back = None
            elif current == node.back:
                node.back = current.prev
                if node.back:
                    node.back.next = None
                else:
                    node.back = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
        current = current.next
        
        


def main():
    tst2 = DoublyLinkedList()
    tst2.push_front(15)
    tst2.push_front(5)
    tst2.push_front(80)
    tst2.push_front(55)
    tst2.push_front(30)
    tst2.push_front(25)
    tst2.push_front(20)
    tst2.push_front(10)
    tst = DoublyLinkedList()
    tst.push_front(10)
    tst.push_front(7)
    tst.push_front(31)
    tst.push_front(25)
    tst.push_front(36)
    tst.push_front(105)
    tst.push_front(0.1)
    tst.push_front(0.01)
    
    run = True
    list_target = None
    while run is True:
        print('Choose list:')

        list_target_input = input('#1 - tst \n #2 - tst2 \n') 
        if list_target_input == '1':
            list_target = tst
        elif list_target_input == '2':
            list_target = tst2
        list_target.print_list()
        print('Choose option')
        print('#1 Add')
        print('#2 Update')
        print('#3 Remove')
        print('#9 Print')
        print('#0 Quit')
        opt = int(input("Select: "))
        if opt == 0:
            run = False
        if opt == 1:
            new_data = int(input('Input new number to add: '))
            list_target.push_front(new_data)
            list_target.print_list()
        if opt == 2:
            target = float(input('Input target to change: '))
            new_data = float(input('Input new data: '))
            update_data(list_target, target,new_data)
            list_target.print_list()
        if opt == 3:
            rm = float(input('Insert number to remove: '))
            remove_data(list_target, rm)
            list_target.print_list()
        if opt == 9:
            list_target.print_list()
            
            
            

        
        
            
if __name__ == "__main__":
    main()