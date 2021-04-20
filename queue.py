from array import *

queue = array('i', [])
rear = 0
front = 0
maxq = 10

def insert():
    global rear
    global maxq
    if rear > maxq:
        print("Queue is full")
    else:
        x = int(input("Enter the Element: "))
        queue.append(x)
        rear = rear + 1

def delete():
    global rear, front
    if rear == front:
        print("Queue is empty")
    else:
        print("The deleted value: ", queue[front])
        front = front + 1


def display():
    global rear, front
    if rear == front:
        print("Queue is empty")
    else:
        print("Queue values: ")
        for i in range(front, rear):
            print(queue[i])

def choice():
    print("1-Insert\n2-Delete\n3-Display\n4-Exit")
    n = int(input("Enter the Choice: "))
    while n < 5:
        if n == 1:
            insert()
            break
        elif n == 2:
            delete()
            break
        elif n == 3:
            display()
            break
        elif n == 4:
            exit()
            break
        else:
            print("Invalid Choice")
            break
    ch = input("Do you want to continue(y/n): ")
    if ch == 'y' or ch == 'Y':
        choice()
    else:
        exit()
