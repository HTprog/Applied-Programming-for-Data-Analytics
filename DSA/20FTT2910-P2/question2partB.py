#Muhammad Hidayat Hidayat Bin Mohd Yusof
#20FFTT2910
#DA3306 DATA STRUCTURES AND ALGORITHMS

import Queue2
Counter1=Queue2.Queue2()
Counter2=Queue2.Queue2()

def remove(counter):
    counter='Counter '+str(counter)
    if counter=='Counter 1':
        Counter1.dequeue()
    elif counter=='Counter 2':
        Counter2.dequeue()
    else:
        print('"'+counter+'"'+' does not exist.')

def counterqueue(x,y):
    customer=str(x)
    counter=y
    if counter==1:
        Counter1.enqueue(customer)
    else:
        Counter2.enqueue(customer)

def listqueue():
    c_queue1=[]
    c_queue2=[]

    if Counter1.is_empty()==True:
        print('Counter 1 queue order: No Customer')

    else:
        for i in range(Counter1.size()):
            c_queue1.append(Counter1.dequeue())
        print('Counter 1 queue order:',c_queue1)

    if Counter2.is_empty()==True:
        print('Counter 2 queue order: No Customer')

    else:
        for i in range(Counter2.size()):
            c_queue2.append(Counter2.dequeue()) 
        print('Counter 2 queue order:',c_queue2)  
   


counterqueue('Customer 1',1)
counterqueue('Customer 2',2)
counterqueue('Customer 3',1)

remove(2)
counterqueue('Customer 2',1)
listqueue()