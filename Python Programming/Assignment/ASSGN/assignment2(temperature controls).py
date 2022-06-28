#import username and welcome the user.
import os
print(f'Welcome, {os.getlogin()}!\n')

#Display "Ice Maker","Adjustable Shelves","LED Display","Temperature Controls","Convertible Fridge","Setting" on the Home screen.
display = ["Ice Maker","Adjustable Shelves","LED Display","Temperature Controls","Convertible Fridge","Setting"]
print(display)
choice = input("\nSelect your choice from above. ")

#If user choose "Temperature Controls", the functions will go to "Temperature Controls" script.
if choice == "Ice Maker":
    print("\nIce Maker")

elif choice == "Adjustable Shelves":
    print("Adjustable Shelves")
    import adjustabeshelves
    
elif choice == "LED Display":
    print("LED Display")

elif choice == "Temperature Controls":
    print("\n[Temperature Controls]")
    import Temperature_Controls
    #should we loop back to choices of features here?

elif choice == "Convertible Fridge":
    print("Convertible Fridge")

else:
    print("Setting")
