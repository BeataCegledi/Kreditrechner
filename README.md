# 💳 Kreditrechner

Konsolenprogramm zur Kreditprüfung und Ratenplan-Berechnung – entwickelt im Rahmen der Berufsschulausbildung zur Fachinformatikerin.

## Funktionsumfang

Das Programm prüft, ob ein Kredit genehmigt werden kann, und gibt bei Genehmigung einen detaillierten monatlichen Ratenplan aus.

### Eingaben
- Kreditbetrag (1 – 100.000 €)
- Laufzeit in Monaten (max. 240)
- Monatliches Nettoeinkommen
- Schufa-Status (ja/nein)
- Kundentyp (VIP / Student / Standard / Sonstige)

### Zinsregeln
| Kundentyp | Jahreszins |
|---|---|
| VIP | 3% |
| Student | 5% |
| Standard | 8% |
| Sonstige | 10% |

### Genehmigungsregeln
- Schufa muss positiv sein
- Monatliche Tilgung darf max. 35% des Einkommens betragen
- VIP oder Student mit Kredit < 2.000 € → keine Bearbeitungsgebühr
- Alle anderen → +1% Bearbeitungsgebühr auf den Kreditbetrag

## Verwendete Python-Konzepte
- `while`-Schleife (Eingabevalidierung + Hauptlogik)
- `for`-Schleife (Ratenplan)
- `try` / `except` (Fehlerbehandlung)
- `if` / `elif` / `else` (Verzweigungen)
- Logische Operatoren (`and`, `or`)
- f-Strings (formatierte Tabellenausgabe)

## Ausführen

```bash
python kredit.py
```

> Voraussetzungen: Python 3.x, keine externen Bibliotheken
