def game():
    while True:
        print("Welcome Warrior")
        name = input("What is your name?")
        print(name + ", you have been chosen by your Earl to raid a neighboring territory.")


        health = 100
        reputation = 50
        position = None

        weapon_choice = input("Please choose your weapon: \n 1. Axe \n 2. Sword \n 3. Longbow ")
        if weapon_choice == 1:
            position = "Forward Assault"
            print("Good choice Warrior. Because you chose the axe, your earl has positioned you in " + position + ".")
        elif weapon_choice == 2:
            position = "Second Wave"
            print("Good choice Warrior. Because you chose the sword, your earl has positioned you in " + position + ".")
        else:
            position = "Hilltop"
            print("Good choice Warrior. Because you chose the longbow, your earl has positioned you in " + position + ".")


        input("Press enter to continue")

        print("You are called to the Great Hall for a feast")

        input("Press enter to continue")

        print("A drunken warrior approaches you with another horn of ale just as you are ready to retire.")
        party_choice = input("Do you: \n 1. Decline and retire to your lodging. \n 2. Take him up on his offer. ")
        if party_choice == 1:
            print("You decline the warrior's offer and stumble home.")
            reputation = reputation - 10
            print("Your choice has cause your reputation among your fellow warriors to decrease.")
            print("Your reputation is now, ", reputation)
        else:
            print("Skol!")
            reputation = reputation + 10
            print("Your choice has caused your reputation among your fellow warriors to increase.")
            print("Your reputation is now, " , reputation)

        input("Press enter to continue")
        print("       ~~ Day of Raid ~~   ")

        if party_choice == 1:
            print("You awake the next morning refreshed and ready for battle.")
            print(health)
            print(reputation)
        else:
            print("You are startled awake by your friend, who angrily tosses you your armour.")
            health = health - 5
            print(health)
            reputation = reputation - 5
            print(reputation)

        
        play_again = input("Would you like to play again, " + name + "?")
        if play_again == "yes" or "y":
            game()
        else:
            exit()

        