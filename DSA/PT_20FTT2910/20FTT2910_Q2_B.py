

Text="PA$$WORD12"
Alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Alphal=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num=[1,2,3,4,5,6,7,8,9,0]
for char in Text:
    if char in Alpha or char in Alphal:
        print(char,'is a letter')
    elif char in num:
        print(char,'is a number')
    else:
        print(char,'is a symbol')