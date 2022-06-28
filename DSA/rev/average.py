from email.errors import FirstHeaderLineIsContinuationDefect
from inspect import formatargvalues

from numpy import average


array=[3,4,5,9]
half=int(len(array)/2)
fhalf=[]
shalf=[]
for i in range(0,half,1):
    fhalf.append(array[i])

for i in range(half,len(array),1):
    shalf.append(array[i])

favg=sum(fhalf)/len(fhalf)
savg=sum(shalf)/len(shalf)

if favg>savg:
    print('first half =',favg)
else:
    print('second half =',savg)
