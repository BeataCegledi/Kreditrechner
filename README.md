# Projekt: „Kredit- & Ratenplan-Rechner“
Du programmierst ein Konsolenprogramm, das prüft, ob ein Kredit möglich ist und (wenn ja) einen einfachen Ratenplan ausgibt.

## Anforderungen:
•
Python als Taschenrechner (Zinsen, Summen, Raten)
•
Verkettung von Ausgaben
•
Einfache Verzweigung
•
Mehrfache Verzweigung
•
Logische Operatoren
•
Geschachtelte Verzweigung
•
For-Schleife
•
Formatierte Ausgaben

## Aufgabenstellung
1) Eingaben
Lasse den Benutzer diese Eingaben tätigen:
kreditbetrag (z. B. 3500)
monate (z. B. 12)
monatliches_einkommen (z. B. 1800)
schufa_ok (True/False)
kundentyp ("standard", "student", "vip")
2) Zinssatz bestimmen
Bestimme den Zinssatz abhängig vom kundentyp:
"vip" → 3% pro Jahr
"student" → 5% pro Jahr
"standard" → 8% pro Jahr
sonst → 10% (Fallback)
➔
if / elif / else
3) Monatliche Rate berechnen
Rechne zunächst:
Jahreszins in Monatszins um: monatszins = jahreszins / 12
Gesamtzinsen grob (einfaches Modell): zinsen = kreditbetrag * (jahreszins/100) * (monate/12)
Gesamtbetrag: gesamt = kreditbetrag + zinsen
Rate: rate = gesamt / monate
4) Kredit-Vorprüfung
Kredit wird nur genehmigt, wenn:
schufa_ok True ist UND
die Rate höchstens 35% des Einkommens ist
➔
Nutze and, ggf. not
Wenn abgelehnt: passende Meldung ausgeben und Programm beenden (oder einfach nichts weiter berechnen).
5) Bonus-Entscheidung
Wenn genehmigt:
Wenn kundentyp == "vip" oder (kundentyp == "student" und kreditbetrag < 2000):
Ausgabe: „Bearbeitungsgebühr entfällt!“
sonst:
Bearbeitungsgebühr = 1% vom Kreditbetrag hinzufügen
➔
or und geschachtelte ifs
6) For-Schleife: Ratenplan ausgeben
Gib für jeden Monat eine Zeile aus:
Monat 1: Rate, Restschuld
Monat 2: Rate, Restschuld
...
(vereinfacht: Restschuld = Restschuld - Rate)
Nutze:
for monat in range(1, monate + 1):
...
7) Formatierte Ausgabe
Am Ende eine „Zusammenfassung“:
Kreditbetrag
Zinssatz
Gesamtkosten
Rate pro Monat
Alles schön formatiert, z. B. :.2f
Mini-Hinweise:
Du brauchst keine Listen
Du kannst Restschuld als Variable führen: rest = gesamt
Verwende einmal Verkettung (mit +) und später formatierte Strings
