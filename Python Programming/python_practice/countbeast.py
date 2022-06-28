name=input("What is your first name? ")
lower=name.lower()
count1=lower.count("a")
count2=lower.count("e")
count3=lower.count("i")
count4=lower.count("o")
count5=lower.count("u")
print("Your name contains the following vowels:\n"+"a:",count1,"\ne:",count2,"\ni:",count3,"\no:",count4,"\nu:",count5,
"\nIn total your name contains ",(count1+count2+count3+count4+count5),"vowels")