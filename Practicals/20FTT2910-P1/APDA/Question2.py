#Muhammad Hidayat Hidayat Bin Mohd Yusof
#20FFTT2910
#DA3304 APPLIED PROGRAMMING FOR DATA ANALYTICS
import pandas as pd
import numpy as np

input1=int(input('Enter a number: '))
array1=np.array(input1)
print(array1)
input2=int(input('Enter a another number: '))
array2=np.array(input2)
print(array2)
input3=input('Enter either +,-,* or /')
if input3=='+':
    print('Answer=',np.add(array1,array2))
elif input3=='-':
    print('Answer=',np.subtract(array1,array2))
elif input3=='*':
    print('Answer=',np.multiply(array1,array2))
elif input3=='/':
    print('Answer=',np.divide(array1,array2))
else:
    print('Invalid input')