# queue using linked list in python
class Node :
    def __init__(self,value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.n = 0

    def enqueue (self,value):

        new_node  = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front 
            
            return 
        
        else:
            self.rear.next = new_node
            self.rear = new_node 

        self.n+=1
        return 


    def dequeue (self):
        dequeued_num = self.front.data
        print('\n')
        print(   dequeued_num , 'is dequeued')

        self.front = self.front.next 
        self.n -= 1
        return
    
    def isEmpty(self):
        return self.rear == None
    
    def size(self):
        return self.n

            

    def traverse(self):
        if self.rear == 0:
            print('Queue is Empty')
            return
        else:
            curr = self.front

            while curr != None:
                print(curr.data , end = " ")            
                curr = curr.next 
        return "Current queue"
                

                

que = Queue()

que.enqueue(1)

que.enqueue(4)
que.enqueue(2)
que.enqueue(3)
que.enqueue(5)
que.enqueue(6)
 
que.traverse()
que.dequeue()
que.traverse()

        


           

        

           