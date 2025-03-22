
# Queue Implementation Using Linked List in Python

This repository contains a simple implementation of a queue data structure using a linked list in Python. A queue follows the First In First Out (FIFO) principle, meaning that the first element added to the queue will be the first one to be removed.

## Table of Contents
- [Classes](#classes)
  - [Node Class](#node-class)
  - [Queue Class](#queue-class)
- [Methods](#methods)
  - [enqueue(value)](#enqueuevalue)
  - [dequeue()](#dequeue)
  - [isEmpty()](#isempty)
  - [size()](#size)
  - [traverse()](#traverse)
- [Usage](#usage)

## Classes 

### Node Class
The `Node` class represents a single node in the linked list. Each node contains:
- `data`: The value stored in the node.
- `next`: A pointer to the next node in the linked list.

```python
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
```

### Queue Class
The `Queue` class manages the queue operations. It contains:
- `front`: A pointer to the front node of the queue.
- `rear`: A pointer to the rear node of the queue.
- `n`: An integer to keep track of the number of elements in the queue.

```python
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.n = 0
```

## Methods

### `enqueue(value)`
This method adds a new element to the rear of the queue.
- If the queue is empty, both `front` and `rear` pointers are set to the new node.
- If the queue is not empty, the `next` pointer of the current `rear` node is updated to point to the new node, and then the `rear` pointer is updated to the new node.

### `dequeue()`
This method removes and returns the element at the front of the queue.
- It prints the dequeued element and updates the `front` pointer to the next node in the queue.
- The size of the queue is decremented by 1.

### `isEmpty()`
This method checks if the queue is empty.
- Returns `True` if the queue is empty (i.e., `rear` is `None`), otherwise returns `False`.

### `size()`
This method returns the current number of elements in the queue.

### `traverse()`
This method prints all the elements in the queue from front to rear.
- If the queue is empty, it prints a message indicating that the queue is empty.

## Usage
Here is an example of how to use the `Queue` class:

```python
que = Queue()

que.enqueue(1)
que.enqueue(4)
que.enqueue(2)
que.enqueue(3)
que.enqueue(5)
que.enqueue(6)

que.traverse()  # Output: 1 4 2 3 5 6
que.dequeue()   # Output: 1 is dequeued
que.traverse()  # Output: 4 2 3 5 6
```

## Conclusion
This implementation provides a basic understanding of how queues can be implemented using linked lists in Python. You can extend this implementation by adding more features such as error handling for dequeue operations on an empty queue or implementing a circular queue.

---

