# =============================================================================
# Kreditrechner
# Autor: Beata Cegledi
# Beschreibung: Konsolenprogramm zur Kreditpruefung und Ratenplan-Berechnung.
#               Der Nutzer gibt Kreditbetrag, Laufzeit, Einkommen,
#               Schufa-Status und Kundentyp ein. Das Programm prueft,
#               ob ein Kredit moeglich ist und gibt einen Ratenplan aus.
#
# Konzepte: while, for, try/except, if/elif/else, logische Operatoren,
#           f-Strings, formatierte Ausgabe
# =============================================================================

running = True  # Steuert die Hauptschleife

while running:

    # --- Kreditbetrag ---
    # Erlaubter Bereich: 1 bis 100.000 EUR
    while running:
        try:
            kredit = int(input("Wie gross soll dein Kredit sein (EUR)? "))
            if 0 < kredit <= 100000:
                break
            else:
                print("\nKreditbetrag muss zwischen 1 und 100.000 EUR liegen.")
        except ValueError:
            print("\nBitte nur Zahlen eingeben!")

    print("\n------------------------------------\n")

    # --- Laufzeit in Monaten ---
    # Maximal 240 Monate (20 Jahre)
    while running:
        try:
            monate = int(input("Fuer wie viele Monate? (max. 240): "))
            if 0 < monate <= 240:
                break
            else:
                print("\nLaufzeit muss zwischen 1 und 240 Monaten liegen.")
        except ValueError:
            print("\nBitte nur Zahlen eingeben!")

    print("\n------------------------------------\n")

    # --- Monatliches Einkommen ---
    while running:
        try:
            einkommen = int(input("Monatliches Nettoeinkommen (EUR)? "))
            if 0 < einkommen <= 25000:
                break
            else:
                print("\nEinkommen muss zwischen 1 und 25.000 EUR liegen.")
        except ValueError:
            print("\nBitte nur Zahlen eingeben!")

    print("\n------------------------------------\n")

    # --- Schufa-Pruefung ---
    # Bei negativer Schufa: kein Kredit moeglich
    while running:
        schufa = input("Ist deine Schufa in Ordnung? (j/n): ").lower()
        if schufa == "j":
            break
        elif schufa == "n":
            exit("\nLeider ist mit negativer Schufa kein Kredit moeglich.\n")
        else:
            print("\nBitte nur j oder n eingeben.")

    print("\n------------------------------------\n")

    # --- Kundentyp und Zinssatz ---
    # VIP: 3% p.a. | Student: 5% p.a. | Standard: 8% p.a. | Sonstige: 10% p.a.
    while running:
        print("Welcher Kundentyp bist du?")
        print("1: VIP      (3% Zinsen)")
        print("2: Student  (5% Zinsen)")
        print("3: Standard (8% Zinsen)")
        print("4: Sonstige (10% Zinsen)")
        try:
            kundentyp = int(input("\nBitte waehlen (1-4): "))
            if kundentyp == 1:
                zinssatz = 0.03 / 12
                break
            elif kundentyp == 2:
                zinssatz = 0.05 / 12
                break
            elif kundentyp == 3:
                zinssatz = 0.08 / 12
                break
            elif kundentyp == 4:
                zinssatz = 0.10 / 12
                break
            else:
                print("\nBitte eine Zahl zwischen 1 und 4 eingeben.")
        except ValueError:
            print("\nBitte nur Zahlen eingeben.")

    print("\n------------------------------------\n")

    # --- Kreditpruefung ---
    # Die monatliche Tilgung darf maximal 35% des Einkommens betragen
    tilgung = kredit / monate
    if tilgung > einkommen * 0.35:
        print("\nDein Einkommen reicht fuer diesen Kreditbetrag leider nicht aus.\n")
        running = False

    while running:

        # --- Bearbeitungsgebuehr ---
        # VIP oder Student mit Kredit < 2.000 EUR: keine Gebuehr
        # Alle anderen: +1% auf den Kreditbetrag
        if kundentyp in (1, 2) and kredit < 2000:
            print("\nBearbeitungsgebuehr entfaellt!\n")
        else:
            kredit *= 1.01
            print("\nBearbeitungsgebuehr (1%) wurde dem Kreditbetrag hinzugefuegt.\n")

        # --- Ratenplan (for-Schleife) ---
        # Fuer jeden Monat: Rate = Tilgung + Zinsen auf Restschuld
        restschuld = kredit
        tilgung = kredit / monate
        print(f"\n{'Monat':>5} | {'Rate (EUR)':>10} | {'Restschuld (EUR)':>16}")
        print("-" * 38)
        for i in range(1, monate + 1):
            zinsen = restschuld * zinssatz
            rate = tilgung + zinsen
            restschuld -= tilgung
            print(f"{i:5}. Monat | {rate:10.2f} | {max(restschuld, 0):16.2f}")

        running = False
