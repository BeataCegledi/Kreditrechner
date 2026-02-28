# 💳 Kreditrechner

> Konsolenprogramm zur Kreditprüfung und Ratenplan-Berechnung – entwickelt im Rahmen der Berufsschulausbildung zur Fachinformatikerin Anwendungsentwicklung.

## 📋 Projektbeschreibung

Dieses Programm simuliert eine vereinfachte Bankanwendung zur Kreditvergabe. Es prüft anhand von Einkommens- und Schufa-Daten, ob ein Kredit genehmigt werden kann, und berechnet bei Genehmigung einen detaillierten monatlichen Ratenplan – inklusive Zinsen, Bearbeitungsgebühr und kundenabhängigem Zinssatz.

## 🚀 Funktionsumfang

### Eingaben
- Kreditbetrag (1 – 100.000 €)
- Laufzeit in Monaten (1 – 240 Monate / max. 20 Jahre)
- Monatliches Nettoeinkommen
- Schufa-Status (positiv / negativ)
- Kundentyp (VIP / Student / Standard / Sonstige)

### Genehmigungsregeln
| Bedingung | Ergebnis |
|---|---|
| Negative Schufa | Kredit abgelehnt |
| Tilgung > 35% des Einkommens | Kredit abgelehnt |
| Alle Bedingungen erfüllt | Ratenplan wird ausgegeben |

### Zins- und Gebührenregeln
| Kundentyp | Jahreszins | Bearbeitungsgebühr |
|---|---|---|
| VIP | 3% | Entfällt bei Kredit < 2.000 € |
| Student | 5% | Entfällt bei Kredit < 2.000 € |
| Standard | 8% | +1% auf Kreditbetrag |
| Sonstige | 10% | +1% auf Kreditbetrag |

### Ausgabe
- Monatlicher Ratenplan als formatierte Tabelle
- Spalten: Monat · Rate (EUR) · Restschuld (EUR)

## 🧠 Verwendete Python-Konzepte

| Konzept | Anwendung im Projekt |
|---|---|
| `while`-Schleife | Hauptlogik + alle Eingabevalidierungen |
| `for`-Schleife | Ratenplan-Berechnung und -Ausgabe |
| `try` / `except` | Fehlerbehandlung bei Nutzereingaben |
| `if` / `elif` / `else` | Kreditprüfung + Zinssatz-Auswahl |
| Logische Operatoren | `and`, `in` für kombinierte Bedingungen |
| f-Strings | Formatierte Tabellenausgabe mit Ausrichtung |
| Mathematische Formeln | Annuitätenberechnung (Tilgung + Zinsen) |

## ▶️ Ausführen

```bash
python kredit.py
```

> **Voraussetzungen:** Python 3.x · Keine externen Bibliotheken nötig

## 👩‍💻 Über die Entwicklerin

Dieses Projekt zeigt meine Fähigkeit, praxisnahe Berechnungslogik mit realistischen Geschäftsregeln in Python umzusetzen – inklusive vollständiger Eingabevalidierung und formatierter Ausgabe.
