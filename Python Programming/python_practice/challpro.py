firstname=(input("What is your first name? ")).title()
lastname=(input("What is your last name? ")).title()
full=firstname+" "+lastname #ive decided to title the first two variables individually because I want the inititals to be in uppercase
length=len(firstname+lastname) #I concatenate the first two variables here instead of just using "full" so i can avoid the space
indexfirst=firstname[0]
indexlast=lastname[0]
initials=indexfirst+indexlast
print("Hello "+full+". Your name contains",length,"letters. With the initials "+initials+".")