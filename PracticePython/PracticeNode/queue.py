size = 5
class Queue:
    def __init__(self):
        self.data = [None] * size
        self.front = 0 
        self.back = 0 
        self.total_data = 0
        
    def enqueue(self, data):
            if self.total_data < size:
                self.data[self.back] = data
                self.back  = (self.back +1)%size
                self.total_data += 1
            else:
                print('Queue is full')
                
    def printQ(self):
        it = self.front
        while it < self.total_data:
            print(self.data[it])
            it +=1



def main():
    d = Queue()
    d.enqueue(2)
    d.enqueue(7)
    d.printQ()

if __name__ == "__main__":
    main()