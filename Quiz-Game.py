def space():
    print("")
    print("")
    print("")

def smallspace():
    print("")
    print("")

def rulez():
    space()
    print("voor we beginnen ga ik je de regels van het spel uitleggen. animal is een text based dieren quiz waar je 3 levens hebt als je levens op zijn dan word het spel herstart. elke vraag is gebaseerd op een dier het doel is om te raden welk dier het is. we wensen je veel plezier :) ")
    space()

aantallevens = int(3)
punten = int(0)

space()
print("welkom bij animal quiz je hebt nu " +  str(aantallevens)  + " levens")
rulez()
start = input('wil je met de game starten?')
if start == "ja":
    space()
    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten" )
    space()
    vr1 = input('welke slang is het grootst ')
    if vr1 == "groene anaconda":
        print("")
        print("correct!")
        print("")
        punten = punten + 1
        smallspace()
        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
        space()
        vr2 = int(input('hoelang leeft de groenlandse walvis '))
        if vr2 >= 200:
            print("")
            print("correct!")
            smallspace()
            punten = punten + 1
            print("")
            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
            space()
            vr3 = input('wat is het snelste dier op aarde ')
            if vr3 == "jachtluipaard":
                print("")
                print("correct!")
                smallspace|()
                punten = punten + 1
                print("")
                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                spcae()
                vr4 = int(input('wat is het langste day haften leven? '))
                if vr4 < 2:
                    print("")
                    print("correct!")
                    smallspace()
                    punten = punten + 1
                    print("")
                    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                    space()
                    vr5 = input('wat is de snelste vogel ')
                    if vr5 == "slechtvalk":
                        print("")
                        print("correct!")
                        smallspace()
                        punten = punten + 1
                        print("")
                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                        space()
                        vr6 = int(input('hoeveel eieren legt een vogelspin '))
                        if vr6 >=100:
                            print("")
                            print("correct!")
                            smallspace()
                            punten = punten + 1
                            print("")
                            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                            space()
                            vr7 = input('wat drinkt een koe ')
                            if vr7 == "water":
                                print("")
                                print("correct!")
                                smallspace()
                                punten = punten + 1
                                print("")
                                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                space()
                                vr8 = input('hoe noem je een baby schaap ')
                                if vr8 == "lammetje":
                                    print("")
                                    print("correct!")
                                    smallspace()
                                    punten = punten + 1
                                    print("")
                                    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                    space()
                                    vr9 = int(input('in welk jaar is de gorilla ontdekt '))
                                    if vr9 == 1902:
                                        print("")
                                        print("correct!")
                                        smallspace()
                                        punten = punten + 1
                                        print("")
                                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                        space()
                                        vr10 = input('welke kleur zijn baby flamingos ')
                                        if vr10 == "lichtgrijs":
                                            space()
                                            punten = punten + 1
                                            print("")
                                            print("gefeliciteerd je hebt quiz gane uitgespeeld je hebt gewonnen met  " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                            space()                                   
    else:
        print("")
        print("helaas is je antwoord fout")
        print("")
        aantallevens = aantallevens - 1
        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
        print("")
        vr2 = int(input('hoelang leeft de groenlandse walvis'))
        if vr2 >= 200:
            print("")
            print("correct!")
            smallspace()
            punten = punten + 1
            print("")
            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
            space()
            vr3 = input('wat is het snelste dier op aarde')
            if vr3 == "jachtluipaard":
                print("")
                print("correct!")
                smallspace()
                punten = punten + 1
                print("")
                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                space()
                vr4 = int(input('wat is het langste day haften leven?'))
                if vr4 < 2:
                    print("")
                    print("correct!")
                    smallspace()
                    punten = punten + 1
                    print("")
                    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                    space()
                    vr5 = input('wat is de snelste vogel')
                    if vr5 == "slechtvalk":
                        print("")
                        print("correct!")
                        smallspace()
                        punten = punten + 1
                        print("")
                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                        space()
                        vr6 = int(input('hoeveel eieren legt een vogelspin'))
                        if vr6 >=100:
                            print("")
                            print("correct!")
                            space()
                            punten = punten + 1
                            print("")
                            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                            space()
                            vr7 = input('wat drinkt een koe')
                            if vr7 == "water":
                                print("")
                                print("correct!")
                                smallspace()
                                punten = punten + 1
                                print("")
                                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                space()
                                vr8 = input('hoe noem je een baby schaap')
                                if vr8 == "lammetje":
                                    print("")
                                    print("correct!")
                                    smallspace()
                                    punten = punten + 1
                                    print("")
                                    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                    space()
                                    vr9 = int(input('in welk jaar is de gorilla ontdekt'))
                                    if vr9 == 1902:
                                        print("")
                                        print("correct!")
                                        space()
                                        punten = punten + 1
                                        print("")
                                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                        space()
                                        vr10 = input('welke kleur zijn baby flamingos')
                                        if vr10 == "lichtgrijs":
                                            space()
                                            
                                            punten = punten + 1
                                            print("")
                                            print("gefeliciteerd je hebt quiz gane uitgespeeld je hebt gewonnen met  " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                            space()                                
        else:
            print("")
            print("helaas is je antwoord fout")
            print("")
            aantallevens = aantallevens - 1
            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
            print("")
            vr3 = input('wat is het snelste dier op aarde')
            if vr3 == "jachtluipaard":
                print("")
                print("correct!")
                space()
                punten = punten + 1
                print("")
                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                space()
                vr4 = int(input('wat is het langste day haften leven?'))
                if vr4 < 2:
                    print("")
                    print("correct!")
                    smallspace()
                    punten = punten + 1
                    print("")
                    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                    space()
                    vr5 = input('wat is de snelste vogel')
                    if vr5 == "slechtvalk":
                        print("")
                        print("correct!")
                        smallspace()
                        punten = punten + 1
                        print("")
                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                        space()
                        vr6 = int(input('hoeveel eieren legt een vogelspin'))
                        if vr6 >=100:
                            print("")
                            print("correct!")
                            smallspace()
                            punten = punten + 1
                            print("")
                            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                            space()
                            vr7 = input('wat drinkt een koe')
                            if vr7 == "water":
                                print("")
                                print("correct!")
                                smallspace()
                                punten = punten + 1
                                print("")
                                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                space()
                                vr8 = input('hoe noem je een baby schaap')
                                if vr8 == "lammetje":
                                    print("")
                                    print("correct!")
                                    smallspace()
                                    punten = punten + 1
                                    print("")
                                    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                    space()
                                    vr9 = int(input('in welk jaar is de gorilla ontdekt'))
                                    if vr9 == 1902:
                                        print("")
                                        print("correct!")
                                        smallspace()
                                        punten = punten + 1
                                        print("")
                                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                        space()
                                        vr10 = input('welke kleur zijn baby flamingos')
                                        if vr10 == "lichtgrijs":
                                            space()
                                            punten = punten + 1
                                            print("")
                                            print("gefeliciteerd je hebt quiz gane uitgespeeld je hebt gewonnen met  " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                            space()
            else:
                print("")
                print("helaas is je antwoord fout")
                print("")
                aantallevens = aantallevens - 1
                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                print("")
                if aantallevens < 1:
                    space()
                    print("game over!")
                else:
                    vr4 = int(input('wat is het langste day haften leven?'))
                    if vr4 < 2:
                        print("")
                        print("correct!")
                        smallspace()
                        punten = punten + 1
                        print("")
                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                        space()
                        vr5 = input('wat is de snelste vogel')
                        if vr5 == "slechtvalk":
                            print("")
                            print("correct!")
                            smallspace()
                            punten = punten + 1
                            print("")
                            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                            space()
                            vr6 = int(input('hoeveel eieren legt een vogelspin'))
                            if vr6 >=100:
                                print("")
                                print("correct!")
                                smallspace()
                                punten = punten + 1
                                print("")
                                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                space()
                                vr7 = input('wat drinkt een koe')
                                if vr7 == "water":
                                    print("")
                                    print("correct!")
                                    smallspace()
                                    punten = punten + 1
                                    print("")
                                    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                    space()
                                    vr8 = input('hoe noem je een baby schaap')
                                    if vr8 == "lammetje":
                                        print("")
                                        print("correct!")
                                        smallspace()
                                        punten = punten + 1
                                        print("")
                                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                        space()
                                        vr9 = int(input('in welk jaar is de gorilla ontdekt'))
                                        if vr9 == 1902:
                                            print("")
                                            print("correct!")
                                            smallspace()
                                            punten = punten + 1
                                            print("")
                                            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                            space()
                                            vr10 = input('welke kleur zijn baby flamingos')
                                            if vr10 == "lichtgrijs":
                                                space()
                                                punten = punten + 1
                                                print("")
                                                print("gefeliciteerd je hebt quiz gane uitgespeeld je hebt gewonnen met  " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                smallspace()
                    else:
                        print("")
                        print("helaas is je antwoord fout")
                        print("")
                        aantallevens = aantallevens - 1
                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                        print("")
                        if aantallevens < 1:
                            space()
                            print("game over!")
                        else:
                            vr5 = input('wat is de snelste vogel')
                            if vr5 == "slechtvalk":
                                print("")
                                print("correct!")
                                smallspace()
                                punten = punten + 1
                                print("")
                                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                smallspace()
                                vr6 = int(input('hoeveel eieren legt een vogelspin'))
                                if vr6 >=100:
                                    print("")
                                    print("correct!")
                                    smallspace()
                                    punten = punten + 1
                                    print("")
                                    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                    space()
                                    vr7 = input('wat drinkt een koe')
                                    if vr7 == "water":
                                        print("")
                                        print("correct!")
                                        smallspace()
                                        punten = punten + 1
                                        print("")
                                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                        space()
                                        vr8 = input('hoe noem je een baby schaap')
                                        if vr8 == "lammetje":
                                            print("")
                                            print("correct!")
                                            smallspace()
                                            punten = punten + 1
                                            print("")
                                            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                            space()
                                            vr9 = int(input('in welk jaar is de gorilla ontdekt'))
                                            if vr9 == 1902:
                                                print("")
                                                print("correct!")
                                                smallspace()
                                                punten = punten + 1
                                                print("")
                                                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                space()
                                                vr10 = input('welke kleur zijn baby flamingos')
                                                if vr10 == "lichtgrijs":
                                                    space()
                                                    punten = punten + 1
                                                    print("")
                                                    print("gefeliciteerd je hebt quiz gane uitgespeeld je hebt gewonnen met  " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                    smallspace()
                            else:
                                print("")
                                print("helaas is je antwoord fout")
                                print("")
                                aantallevens = aantallevens - 1
                                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                print("")
                                if aantallevens < 1:
                                    space()
                                    print("game over!")
                                else:
                                    vr6 = int(input('hoeveel eieren legt een vogelspin'))
                                    if vr6 >=100:
                                        print("")
                                        print("correct!")
                                        smallspace()
                                        punten = punten + 1
                                        print("")
                                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                        space()
                                        vr7 = input('wat drinkt een koe')
                                        if vr7 == "water":
                                            print("")
                                            print("correct!")
                                            smallspace()
                                            punten = punten + 1
                                            print("")
                                            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                            space()
                                            vr8 = input('hoe noem je een baby schaap')
                                            if vr8 == "lammetje":
                                                print("")
                                                print("correct!")
                                                space()
                                                punten = punten + 1
                                                print("")
                                                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                space()
                                                vr9 = int(input('in welk jaar is de gorilla ontdekt'))
                                                if vr9 == 1902:
                                                    print("")
                                                    print("correct!")
                                                    smallspace()
                                                    punten = punten + 1
                                                    print("")
                                                    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                    space()
                                                    vr10 = input('welke kleur zijn baby flamingos')
                                                    if vr10 == "lichtgrijs":
                                                        space()
                                                        punten = punten + 1
                                                        print("")
                                                        print("gefeliciteerd je hebt quiz gane uitgespeeld je hebt gewonnen met  " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                        smallspace()
                                        else:
                                            print("")
                                            print("helaas is je antwoord fout")
                                            print("")
                                            aantallevens = aantallevens - 1
                                            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                            print("")
                                            if aantallevens < 1:
                                                space()
                                                print("game over!")
                                            else:
                                                vr8 = input('hoe noem je een baby schaap')
                                                if vr8 == "lammetje":
                                                    print("")
                                                    print("correct!")
                                                    space()
                                                    punten = punten + 1
                                                    print("")
                                                    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                    space()
                                                    vr9 = int(input('in welk jaar is de gorilla ontdekt'))
                                                    if vr9 == 1902:
                                                        print("")
                                                        print("correct!")
                                                        smallspace()
                                                        punten = punten + 1
                                                        print("")
                                                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                        space()
                                                        vr10 = input('welke kleur zijn baby flamingos')
                                                        if vr10 == "lichtgrijs":
                                                            space()
                                                            punten = punten + 1
                                                            print("")
                                                            print("gefeliciteerd je hebt quiz gane uitgespeeld je hebt gewonnen met  " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                            space()
                                                else:
                                                    print("")
                                                    print("helaas is je antwoord fout")
                                                    print("")
                                                    aantallevens = aantallevens - 1
                                                    print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                    print("")
                                                    if aantallevens < 1:
                                                        space()
                                                        print("game over!")
                                                    else:
                                                        vr9 = int(input('in welk jaar is de gorilla ontdekt'))
                                                        if vr9 == 1902:
                                                            print("")
                                                            print("correct!")
                                                            space()
                                                            punten = punten + 1
                                                            print("")
                                                            print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                            space()
                                                            vr10 = input('welke kleur zijn baby flamingos')
                                                            if vr10 == "lichtgrijs":
                                                                space()
                                                                punten = punten + 1
                                                                print("")
                                                                print("gefeliciteerd je hebt quiz gane uitgespeeld je hebt gewonnen met  " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                                space()
                                                            else:
                                                                print("")
                                                                print("helaas is je antwoord fout")
                                                                print("")
                                                                aantallevens = aantallevens - 1
                                                                print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                                print("")
                                                                if aantallevens < 1:
                                                                    space()
                                                                    print("game over!")
                                                                else:
                                                                    vr10 = input('welke kleur zijn baby flamingos')
                                                                    if vr10 == "lichtgrijs":
                                                                        space()
                                                                        punten = punten + 1
                                                                        print("")
                                                                        print("gefeliciteerd je hebt quiz gane uitgespeeld je hebt gewonnen met  " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                                        smallspace()
                                                                    else:
                                                                        print("")
                                                                        print("helaas is je antwoord fout")
                                                                        print("")
                                                                        aantallevens = aantallevens - 1
                                                                        print("je hebt nu " + str(aantallevens) + " levens en " + str(punten) + " punten")
                                                                        print("")
                                                                        if aantallevens < 1:
                                                                            space()
                                                                            print("game over!")