# THIS SECTION IM USING SINGLE LINK LIST FRONT -> NODE -> NODE -> NONE
# class Node:
    # def __init__(self, data, next = None):
        # self.data = data
        # self.next = next
        

# class Stack:
    # def __init__(self):
        # self.top = 0
        # self.front = Node(None)
    # def push(self,data):
        # nn = Node(data,self.front.next)
        # self.front.next = nn
        # self.top+=1
    # def pop(self):
        # if self.top > 0:
            # self.front.next = self.front.next.next
            # self.top-=1
        # else:
            # return
    # def topPos(self):
        # return self.top
    
    
# def printStack(stack):
    # current = stack.front.next
    # print('Top: ', stack.topPos())
    # while current:
        # print(current.data)
        # current = current.next
    
    
#THIS SECTION IM USING DOUBLE LINKED LIST WITH FRONT AND BACK
class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
 
class Stack:
    def __init__(self):
        self.front      = Node(None)
        self.back       = Node(None)
        self.front.next = self.back
        self.back.prev  = self.front
        self.top = 0 # we dont need it here but just for practice purpose
        
    def push(self,data):
        nn = Node(data, self.front.next, self.front) # here we set next and previous from parameters so we have a chain to our new node
        if self.front.next == self.back: # if list is empty, it means we have to set our 'back/tail' previous to this new node so we have a reference
            self.back.prev = nn
        else: # otherwise, we just set the previous from the first Node
            self.front.next.prev = nn
        self.front.next = nn # and always set our front next to this new node since its stack
        self.top+=1 # update top size so we can access it (if using raw array)
        
    def printStack(self):
        current = self.front.next
        if current is self.back:
            print("Empty list")
        while current.data is not None: # Since we have a Node inside our List, we can check by the data Node (if it was a class with person we could track by id as well like current.data.id)
            print(current.data ,end= " <->")
            current = current.next
            
    def pop(self):
        if self.front.next == self.back: #make sure our list is not empty
            return
        else: # chain fron to the next.next and previous from next.next to front so the chaint to front -> front.next is removed
            self.front.next = self.front.next.next
            self.front.next.prev = self.front
    
    
def main():
    st = Stack()
    st.push(3)
    st.push(4)
    st.push(7)
    st.pop()
    st.pop()
    st.printStack()
    
if __name__ == "__main__":
    main()