# Introduction and Goals

[comment]: <> (Motivation und Ziel Hinterlegen)

## Requirements Overview

[comment]: <> (Was soll geleistet werden)

# Repo Structure

|__example \
| \
|__sentiment_analysis \
|   | \
|   |__testing \
|   | \
|   |__input \
| \
|__tests \



# Architecture Constraints

[comment]: <> (Weitere Randbedingungen sammeln)
Es sollte Hadoop verwendet werden

# System Scope and Context

[comment]: <> (Architektur Diagramm)

## Business Context

Politische Entscheidungen haben Einfluss auf die Stimmungslage des Landes.
Um das zu bestätigen, werden politische Aussagen mit der Stimmungslagen der jeweiligen Tage in Verbindung gesetzt.

„Sie glauben gar nicht, wenn man jeden Tag direkt neben Angela Merkel am Tisch sitzt, verliert man alle Eigenschaften eines bayerischen Löwen. Man wird wirklich zahm.“ (CSU-Chef Horst Seehofer am 12. Januar nach den Sondierungsgesprächen beim Neujahrsempfang der bayerischen Staatsregierung in der Münchner Residenz.)
Quelle: neuepresse.de

„Deutschland ist nur so erfolgreich, weil es uns Bayern gibt. Das steht fest.“ (Bayerns designierter Ministerpräsident Markus Söder, CSU, am 14. Februar beim politischen Aschermittwoch in Passau.)

"Wir haben Videoaufnahmen darüber, dass es Hetzjagden gab, dass es Zusammenrottungen gab, dass es Hass auf der Straße gab, und das hat mit unserem Rechtsstaat nichts zu tun.“
(Bundeskanzlerin Angela Merkel am 28. August in Berlin zu den Ausschreitungen im sächsischen Chemnitz.)

## Technical Context

Die Ergebnisdatei enthält die polarity für jeden Tag.
Die Tages polarity errechnet sich aus dem Schnitt aller polarity Werte für einen Tag.
Die Daten für diese Rechnung werden ebenfalls übergeben.

| Bundesland | Polarity |
| ---------- | -------- |
| 03.03.2021 | 0.4      |
| 04.03.2021 | 0.2      |
| 05.03.2021 | 0.6      |
| 06.03.2021 | 0.1      |
| 07.03.2021 | 0.8      |
| 08.03.2021 | 0.9      |
| 09.03.2021 | 0.2      |
| 10.03.2021 | 0.52     |
| 11.03.2021 | 0.14     |
| 12.03.2021 | 0.16     |
| 13.03.2021 | 0.61     |
| 14.03.2021 | 0.26     |
| 15.03.2021 | 0.67     |
| 16.03.2021 | 0.72     |
| 17.03.2021 | 0.83     |
| 18.03.2021 | 0.25     |
| 19.03.2021 | 0.6      |

```json
{
  "root": [
    {
      "03.03.2021": {
        "sentiment": 0.6,
        "data": {
          "TweetId": {
            "03.03.2021-01:30": 0.4
          },
          "Twe3tId": {
            "03.03.2021-02:30": 0.8
          }
        }
      }
    },
    {
      "04.03.2021": {
        "sentiment": 0.6,
        "data": {
          "TweetId": {
            "04.03.2021-01:30": 0.4
          },
          "Twe3tId": {
            "04.03.2021-02:30": 0.8
          }
        }
      }
    }
  ]
}
```

# Solution Strategy

[comment]: <> (Wie wird das Projekt umgesetzt)
Das Projekt wird durch die Verwendung einer Sentimentanalyse umgesetzt. Hierzu wird sich primär auf die Programmiersprache Python gestützt (u.a. zur Implementation des WebServers). Da viele Daten umzusetzen sind, wird ein Clustering mit Hadoop durchgeführt.
