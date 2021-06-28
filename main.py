import database as data


while True:
    print("""\nChemie Rechner Tool
    1. Übersicht
    2. Rechner
    3. Credits""")
    mode = input("Modus: ")
    if mode == "1":
        print("""Konstanten:
Avogadro-Konstante = \n6e23
""")
        input("Weiter (Formeln)? ")
        print("""Formeln:
Masse = \nMolare Masse * Stoffmenge; \nm = M * n
""")
        input("Weiter (Formeln 2)? ")
        print("""Absolute Teilchenanzahl = \nStoffmenge * Molare Masse; \nN = n * M """)
        input("Weiter (Variablen 1)? ")
        print("""Formelzeichen:
M = Molare Masse\ng/Mol oder u
m = Masse in g
ma = Atommasse in u 
""")
        input("Weiter (Variablen 2)?")
        print("""Mol = 6*10**23 Teilchen 
N = Absolute Teilchen-\nanzahl; Teilchena
n = Stoffmenge einer\nStoffportion in Mol
Na = Avogadro-Konstante""")
        input("Ende? ")
    
    elif mode == "2":
        def MolareMasseR():
            Masse1 = input('Masse in g:')
            Masse1 = float(Masse1)
            Stoffmenge1 = input('Stoffmenge in Mol: ')
            Stoffmenge1 = int(Stoffmenge1)
            MolareMasse1 = Masse1 / Stoffmenge1
            print(str(MolareMasse1) + 'g/Mol')


        def MasseR():
            while True:
                stoff = input("Hast du einen Stoff? \n(1-Ja / 2-Nein): ")
                if stoff == "1":
                    hatStoff = True
                    break

                elif stoff == "2":
                    hatStoff = False
                    break

            if not hatStoff:
                MolareMasse2 = float(input('Molare Masse in g/Mol: '))
            else:
                MolareMasse2 = input("Element \n(Formelzeichen): ")
                MolareMasse2 = data.Elements[MolareMasse3]["Atommasse"]
            Stoffmenge2 = input('Stoffmenge in Mol: ')
            Stoffmenge2 = float(Stoffmenge2)
            Masse2 = MolareMasse2 * Stoffmenge2
            print(str(Masse2) + 'kg')


        def StoffmengeR():
            while True:
                stoff = input("Hast du einen Stoff?\n (1-Ja / 2-Nein): ")
                if stoff == "1":
                    hatStoff = True
                    break

                elif stoff == "2":
                    hatStoff = False
                    break

            if not hatStoff:
                MolareMasse3 = float(input('Molare Masse \nin g/Mol: '))
            else:
                MolareMasse3 = input("Element (Formelzeichen): ")
                MolareMasse3 = data.Elements[MolareMasse3]["Atommasse"]
            Masse3 = float(input('Masse in g:'))
            Stoffmenge3 = Masse3 / MolareMasse3
            print(str(Stoffmenge3) + 'Mol')
            input("Weiter? ")
            F2 = input('Willst du die \nStoffmenge in die \nabsolute Teilchenanzahl (N) \numrechnen? (1-Ja/2-Nein)')
            if F2 == '1':
                Stoffmenge3 = float(Stoffmenge3)
                AbsoluteTeilchenanzahl = Stoffmenge3 * 6 * (10 ** 23)
                print(AbsoluteTeilchenanzahl)
            else:
                print('OK')

        while True:
            F = input('''Was willst du ausrechnen? 
\tMolare Masse(1) 
\tMasse(2)
\tStoffmenge(3)\nModus: ''')

            try:
                if 1 <= int(F) <= 3:
                    break

            except:
                print("nicht verfügbar")

        if F == '1':
            MolareMasseR()
        elif F == '2':
            MasseR()
        else:
            StoffmengeR()

    elif mode == "3":
        print("""Developed by\nNoname\nBene\nDoctorFuchs""")
        input("Ende? ")
    
    else:
        print("nicht verfügbar!")
