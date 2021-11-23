def space():
    print("")
    print("")
    print("")

def Rules():
    space()
    Gamerule = input('wil je de regels leten?')
    if Gamerule == "yes" or "Yes":
        space()
        print("de animal quiz is een text based quiz game je begint met 3 levens en 0 punten als je levens op zijn stop het spel en zal je zien hoeveel vragen je goed hebt"
        
    elif Gamerule == "Nee" or "nee":
        space()

def game():
    aantallevens = int(3)
    punten = int(0)

    space()
    naam = input('wat is je naam?')

    space()
    print("hallo ",naam," welkom bij de animal quiz dit is een text based quiz spel")
    

    

game()