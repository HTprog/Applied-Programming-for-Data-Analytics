#import username and welcome the user.
import os
import Temperature_Controls
print(f'Welcome, {os.getlogin()}!\n')
savedtemp=0
while True:
    #Display "Ice Maker","Adjustable Shelves","LED Display","Temperature Controls","Convertible Fridge","Setting" on the Home screen.
    display = ["Ice Maker","Adjustable Shelves","LED Display","Temperature Controls","Convertible Fridge","Setting"]
    print(display)
    choice = input("\nSelect your choice from above. ").lower().strip()

    #If user choose "Temperature Controls", the functions will go to "Temperature Controls" script.
    if choice == "ice maker":
        print("\nIce Maker")

    elif choice == "adjustable shelves":
        print("Adjustable Shelves")
        import adjustabeshelves
    elif choice == "LED Display":
        print("LED Display")

    elif choice == "temperature controls":
        print("\n[Temperature Controls]")
        savedtemp=Temperature_Controls.controltemp(savedtemp) 
        
        #should we loop back to choices of features here?

    elif choice == "convertible fridge":
        print("Convertible Fridge")
        print("Current saved temp = ",savedtemp)

    elif choice =="quit":
        break

    else:
        print("Setting")
