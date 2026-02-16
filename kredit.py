running = True
while running: 
# Eingaben:
    
    while running:
        try: 
            kredit = int(input("Wie groß soll dein Kredit sein (€)? "))
            if kredit > 0 and kredit <= 100000:
                break
            else:
                print("\nKredit darf nicht negativ oder mehr als 100 000€ sein")
        except ValueError:
            print("\nBitte nur Zahlen eingeben!")
            continue

    print("\n------------------------------------\n")
    while running:
        try: 
            monate = int(input("Für wieviel Monaten möchtest du aufnehmen (max 240))? "))
            if monate > 0 and monate <= 240:
                break
            else:
                print("\nMonatenzahl darf nicht negativ oder mehr als 240 sein")
        except ValueError:
            print("\nBitte nur Zahlen eingeben!")
            continue

    print("\n------------------------------------\n")
    while running:
        try: 
            einkommen = int(input("Wie groß sind deine Molnatliches Einkommen? "))
            if einkommen > 0 and einkommen <= 25000:
                break
            else:
                print("\nEinkommen darf nicht negativ oder mehr als 25000€ sein")
        except ValueError:
            print("\nBitte nur Zahlen eingeben!")
            continue        

    print("\n------------------------------------\n")
    while running:
        schufa = input("Ist dein Schufa OK (j/n): ").lower()
        if schufa == "j":
            break
        elif schufa == "n":
            exit("\nLeider mit negativer Schufa kein Kredit möglich!\n")
#            running = False
            break
        else:
            print("\nDu darfst nur j oder n eingeben")
        
    print("\n------------------------------------\n")
    while running:
        print("Welche betrifft dich aus den folgenden Kundentypen?")
        print("1: VIP")
        print("2: Student")            
        print("3: Standard")            
        print("4: Sonstiges")
        try: 
            kundentyp = int(input("\nBitte wählen (1-4): "))
            if kundentyp == 1:
                zinssatz = 0.03/12
                break
            elif kundentyp == 2:
                zinssatz = 0.05/12
                break
            if kundentyp == 3:
                zinssatz = 0.08/12
                break
            if kundentyp == 4:
                zinssatz = 0.1/12
                break
            else:
                print("\nDu must einen Zahl zwischen 1 und 4 geben")
                continue
        except ValueError:
            print("\nDu must einen Zahl zwischen 1 und 4 geben")

#  Monatliche Rate berechnen
    restschuld = kredit
    tilgung = kredit / monate
    if tilgung > einkommen*0.35:
        print("\nDein Einkommen reicht für so großen Kreditsumme leider nicht aus!\n")
        running = False
    while running:
# Bearbeitungsgebühr
        if kundentyp in (1,2) and kredit < 2000:
            print("\nBearbeitungsgebühr entfällt!\n")
        else:
            kredit *= 1.01
            print("\n Bearbeitungsgebühr kostet 1% vom Kreditbetrags. Wir haben es zu deinen Kredigt hinzugefügt!\n")

#Monatliche Ratenplan
        restschuld = kredit
        tilgung = kredit / monate
#Rate = tilgung + zinsen
        for i in range(1,monate+1):
            zinsen = restschuld*zinssatz
            rate = tilgung + zinsen
            restschuld -= tilgung
            print("%3i. Monat  | Rate: %8.2f  | Restschuld: %10.2f" % (i, rate, restschuld))
        running = False