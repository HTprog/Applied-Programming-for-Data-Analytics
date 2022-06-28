firstname=(input("What is your first name? ")).title()
lastname=(input("What is your last name? ")).title()
full=firstname+" "+lastname     #ive decided to title the first two variables individually because I want the inititals to be in uppercase
length=len(firstname+lastname)  #I concatenate the first two variables here instead of just using "full" so i can avoid the space
indexfirst=firstname[0]
indexlast=lastname[0]
initials=indexfirst+indexlast

lowercase=full.lower()
count1=lowercase.count("a")
count2=lowercase.count("e")
count3=lowercase.count("i")
count4=lowercase.count("o")
count5=lowercase.count("u")

print("Hello "+full+". Your name contains",length,"letters. With the initials "+initials+
".\nYour name contains the following vowels:\n"+"a:",count1,"\ne:",count2,"\ni:",count3,"\no:",count4,"\nu:",count5,
"\nIn total your name contains ",(count1+count2+count3+count4+count5),"vowels")