from pyparsing import Char, Word


text=input('Please enter text:')
textlist=[]
text=text.replace(' ','')
# splitlist=text.split()
# print(splitlist)
for i in text:
    textlist.append(i)

for i in range(len(textlist)):
    if i%2==0:
        continue
    else:
        print(textlist[i])