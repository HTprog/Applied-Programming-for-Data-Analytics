junction1=input("You see two paths infront of you.\nOne on the left and one on the right."+
"\nWhich path do you take?\n")
if junction1=="Left":
    print("\nYou have come upon another junction\n")
    junction2=input("The path on the left leads to a tunnel that is devoid of light."+
    "\nThe path on the right looks completely normal.\nWhich path do you take?\n") 
    if junction2=="Left":
        print("\nYou have come upon another junction\n")
        junction3=input("This time both left and right paths lead to complete darkness."+
        "\nBut you feel a faint breeze from the path on the right.\nWhich path do you take?\n")
        if junction3=="Right":
            print("The path you took leads to an opening with light coming through."+
            "\nYou go through it and come upon a beach with an abandoned speed boat.\n"+
            "You took the boat and sailed towards home.\nYou have escaped the island!")
        else:
            print("You walk and walk along the path on the left but only see pitch black"
            "\nYou have reached a Dead END")
    else:
        print("You have reached a Dead End")
else:
    print("You have reached a Dead End")