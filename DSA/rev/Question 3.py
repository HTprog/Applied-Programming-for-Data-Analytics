dob=input('Please enter your date of birth(dd:mm:yyyy):')
doblist=dob.rsplit('/')
#print(doblist)

if doblist[1]=='1' or doblist[1]=='01':
    print('January')
if doblist[1]=='2'or doblist[1]=='02':
    print('Febuary')
if doblist[1]=='3' or doblist[1]=='03':
     print('March')
elif doblist[1]=='4'or doblist[1]=='04':
    print('April')
elif doblist[1]=='5'or doblist[1]=='05':
    print('May')
elif doblist[1]=='6'or doblist[1]=='06':
    print('June')
elif doblist[1]=='7'or doblist[1]=='07':
    print('July')
elif doblist[1]=='8' or doblist[1]=='08':
    print('August')
elif doblist[1]=='9' or doblist[1]=='09':
    print('September')
elif doblist[1]=='10':
    print('October')
elif doblist[1]=='11':
    print('November')
elif doblist[1]=='12':
    print('December')

else:
    print('Invalid Month')

age=2022-int(doblist[2])
print('Your age is {}'.format(age))