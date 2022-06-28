list=["A","E","I","O","U"]
name=input("Please enter your name: ")
vowels=0
for i in range(len(name)-1):
    if name[i] in list:
        vowels=vowels+1
print("Hello "+name+" you have",vowels,"vowels in your name")