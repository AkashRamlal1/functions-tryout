def form():

    x = str(input('wat is je naam? ')) #typ je naam
    z = int(input('hoe oud ben je '))    #typ je leeeftijf
    while x != "stop": #als  je stop typt moet de code stoppen
        x = input('wat is je naam? ')
        z = input('hoe oud ben je ')
        print("hallo ",x," je bent", z," jaar oud")

        if x == "":
            print("je hebt geen antwoord ingevul")

form()
