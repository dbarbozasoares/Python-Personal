class Queue:
    def __init__(self):
        self.next_password = 1
        self.size = 2
        self.data = [None] * self.size
        self.front = 0 
        self.back = 0 
        self.total_data = 0
        
    def enqueue(self, data):
            if self.total_data < self.size:
                self.data[self.back] = data
                self.back  = (self.back +1)%self.size
                self.total_data += 1
                self.next_password +=1
            else:
                print('Queue is full')
                
    def printRawQueue(self):
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
            
    def printAllClients(self):
        it = self.front
        count = 0
        while count < self.total_data:
            print('#NAME: ', self.data[it].name, ' #PASSWORD: ', self.data[it].password)
            it = (it+1)%self.size
            count +=1
    def dequeue(self):
        if self.total_data > 0:
            self.front = (self.front+1)%self.size
            self.total_data -= 1
        else:
            print('Empty queue')
        
class Client:
    def __init__(self, name, password = 0):
        self.password = password
        self.name = name
    def getPass(self):
        return self.password
    def getNextPass(self):
        return self.password+1
    def setPassword(self, password):
        self.password = password
    def printClient(self):
        print('#NAME: ', self.name, ' #PASSWORD: ', self.password)
class Store:
    def __init__(self, name = "NoName", size = 3):
        self.name = name
        self.size = size
    
def run(queue = []):
    run = True
    while run is True:
        print('#1 - Add')
        print('#2 - Remove front')
        print('#3 - Print Queue')
        opt = int(input('Selection: '))
        if opt == 1:
            client_name = input('Input name: ')
            client = Client(client_name, queue.next_password)
            queue.enqueue(client)
        if opt == 2:
            queue.dequeue()
        if opt == 3:
            queue.printAllClients()
        
        
def main():
    queue = Queue()
    run(queue)
    

if __name__ == "__main__":
    main()