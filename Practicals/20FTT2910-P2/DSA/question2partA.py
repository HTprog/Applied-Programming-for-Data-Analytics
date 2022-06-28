#Muhammad Hidayat Hidayat Bin Mohd Yusof
#20FFTT2910
#DA3306 DATA STRUCTURES AND ALGORITHMS

import Queue2
Counter1=Queue2.Queue2()
Counter2=Queue2.Queue2()
def counterqueue(x,y):
    customer=str(x)
    counter=y
    if counter==1:
        Counter1.enqueue(customer)
    else:
        Counter2.enqueue(customer)
counterqueue('Customer 1',1)
counterqueue('Customer 2',2)
counterqueue('Customer 3',1)

def listqueue():
    c_queue1=[]
    c_queue2=[]
    for i in range(Counter1.size()):
        c_queue1.append(Counter1.dequeue())
    for i in range(Counter2.size()):
        c_queue2.append(Counter2.dequeue()) 

    print('Counter 1 queue order:',c_queue1)
    print('Counter 2 queue order:',c_queue2)  

listqueue()
