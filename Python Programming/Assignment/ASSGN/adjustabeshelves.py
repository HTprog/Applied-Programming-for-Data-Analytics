
settings = ['Position', 'Locking', 'Alignment']
print(settings)
option = input('Select your option: ')
# This is when user(s) want to reposition the seal and replace the shelves 
# To move the shelves, it can only be up to 3 movements/steps
if option == 'Position':
    position = input('Move up / Move down: ')
    if position == 'Up':
        movement = ['1 step', '2 steps', '3 steps']
        print(movement)
        up = input("Select how many steps (+): \n")
        if up == '1 step':
            print('Shelves moved up by +1.')
        elif up == '2 steps':
            print('Shelves moved up by +2')
        else:
            print('Shelves moved up by +3')
# Same goes like the above process, the shelves can only move down to 3 steps
    else:
        movement = ['1 step', '2 steps', '3 steps']
        print(movement)
        down = input('Select how many steps (-): \n')
        if down == '1 step':
            print('Shelves moved down by -1.')
        elif down == '2 steps':
            print('Shelves moved down by -2.')
        else:
            print('Shelves moved down by -3.')
# After positioned correctly, the shelves are either locked or left unlocked
elif option == 'Locking':
    Locking = input("lock/unlock: ")
    if Locking == "lock":
        print("The shelves are locked.")
    else:
        print("The shelves are unlocked.")
# To ensure the shelves are aligned, clips are used
else:
    alignment = input("Insert clips? Press 1 for Yes, Press 2 for No: \n 1 \n 2 \n")
    if alignment == "1":
        print("Successfully aligned.")
    else:
        print("Shelves are not aligned.")
