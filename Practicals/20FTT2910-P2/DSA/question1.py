#Muhammad Hidayat Hidayat Bin Mohd Yusof
#20FFTT2910
#DA3306 DATA STRUCTURES AND ALGORITHMS

import Stack2

newstack=Stack2.Stack2()

print(newstack.is_empty())
tobeconverted=505
input=tobeconverted
while True:
    quotient=input//2
    remainder=input%2
    if quotient==0:
        newstack.push(1)
        #print(1)
        break
    elif remainder==0:
            newstack.push(0)
            #print(0)
            input=quotient
            continue
    else:
        newstack.push(1)
        #print(1)
        input=quotient
        continue
print('The binary is:')
stacklist=[]
for i in range(newstack.size()):
    stacklist.append(newstack.pop())
converted='0'+''.join(map(str,stacklist))
print('Binary of',tobeconverted,'is',converted)

