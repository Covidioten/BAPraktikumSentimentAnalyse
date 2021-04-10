# Introduction and Goals

This project analysis Twitter data concerning the sentiment of tweet in Germany and compares the data to cases of COVID-19 in Germany. Furthermore, this application displays the political and epidemical situation in Germany in 2020. To just use the application visit [covidioten.app](https://covidioten.app/#/polit).
This is only the repository where the data analysis is stored. For the Frontend visit the [UI repository](https://github.com/Covidioten/UI). 
The Webserver Backend is stored in [webserver repository](https://github.com/Covidioten/WebServer).

# Table of Contents
* [Requirements Overview](#Requirements-Overview)
* [Technologies](#technologies)
* [Execution instructions](#Execution-instructions)
* [Repo Structure](#Repo-structure)
* [Architecture Contraints](#Architecture-Contraints)
* [System Scope and Context](#System-Scope-and-Context)
* [Solution Strategy](#Solution-Strategy)

## Requirements Overview

[comment]: <> (Was soll geleistet werden)

# Execution instructions

Requirements:
- the instructions assume that a Hadoop Cluster has been setup up already and is not covered here

Instructions:
- navigate into sentiment_analysis  
<code>cd sentiment_analysis</code>
- start hadoop job  
<code>hadoop jar /path/to/streaming/jar/hadoop-streaming.jar -files /path/to/tokenmapper/tokenmapper.py,path/to/sumreducer/pathreducer.py -mapper /path/to/tokenmapper/tokenmapper.py -reducer /path/to/sumreducer/sumreducer.py -input /path/to/dataset -output /path/to/output </code>

# Repo Structure

example:  
- contains minimum tokenmapper and sumreducer to get started with  

sentiment_analysis:  
- testing: contains files that were used to test the map/reduce proccess on small amount of data
- output: the output folder of the map/reduce process

tests:  
- unit tests for the sentiment analysis

|__example  
|  
|__sentiment_analysis  
|  |  
|  |__testing  
|  |  
|  |__output  
|  
|__tests  



# Architecture Constraints

[comment]: <> (Weitere Randbedingungen sammeln)
Hadoop should be used

# System Scope and Context

[comment]: <> (Architektur Diagramm)

## Business Context

Political decisions have an influence on the sentiment of a country
To research the impact of these decisions on the sentiment we analyze the correlation between the calculated sentiment and political statements and actions.

„Sie glauben gar nicht, wenn man jeden Tag direkt neben Angela Merkel am Tisch sitzt, verliert man alle Eigenschaften eines bayerischen Löwen. Man wird wirklich zahm.“ (CSU-Chef Horst Seehofer am 12. Januar nach den Sondierungsgesprächen beim Neujahrsempfang der bayerischen Staatsregierung in der Münchner Residenz.)
Quelle: neuepresse.de

„Deutschland ist nur so erfolgreich, weil es uns Bayern gibt. Das steht fest.“ (Bayerns designierter Ministerpräsident Markus Söder, CSU, am 14. Februar beim politischen Aschermittwoch in Passau.)

"Wir haben Videoaufnahmen darüber, dass es Hetzjagden gab, dass es Zusammenrottungen gab, dass es Hass auf der Straße gab, und das hat mit unserem Rechtsstaat nichts zu tun.“
(Bundeskanzlerin Angela Merkel am 28. August in Berlin zu den Ausschreitungen im sächsischen Chemnitz.)

## Technical Context

The result file contains the polarity für each day.
The daily polarity is calculated by taking the average over each day
The data for these calculations is included in the structure aswell

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

The project goals are achived by utilizing sentiment analysis. Python will be the language to implement the neccessary functionality. Because of the huge amount of data to analyze the calculations are run on a hadoop cluster.
