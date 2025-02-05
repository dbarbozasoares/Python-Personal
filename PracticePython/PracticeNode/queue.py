class Queue:
    def __init__(self):
        self.size = 5
        self.data = [None] * self.size
        self.front = 0 
        self.back = 0 
        self.total_data = 0
        
    def enqueue(self, data):
            if self.total_data < self.size:
                self.data[self.back] = data
                self.back  = (self.back +1)%self.size
                self.total_data += 1
            else:
                print('Queue is full')
                
    def printQ(self):
        it = self.front
        count = 0
        while count < self.total_data:
            print(self.data[it])
            it = (it+1)%self.size
            count +=1
    def dequeue(self):
        if self.total_data > 0:
            self.front = (self.front+1)%self.size
            self.total_data -= 1
        else:
            print('Empty queue')
            
            
        



def main():
    d = Queue()
    d.enqueue(2)
    d.enqueue(7)
    d.enqueue(73)
    d.enqueue(99)
    d.dequeue()
    d.dequeue()
    d.printQ()

if __name__ == "__main__":
    main()