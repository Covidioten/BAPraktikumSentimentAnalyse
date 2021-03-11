#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
import re
import datetime

city_arr = ["Berlin", "Hamburg", "München", "Köln", "Frankfurt am Main",
            "Stuttgart", "Düsseldorf", "Dortmund", "Essen", "Leipzig",
            "Bremen", "Dresden", "Hannover", "Nürnberg", "Duisburg",
            "Bochum", "Wuppertal", "Bielefeld",	"Bonn", "Münster"]

bland_arr = ["Baden-Württemberg", "Bayern", "Brandenburg", "Hessen",
            "Mecklenburg-Vorpommern", "Niedersachsen", "Nordrhein-Westfalen",
             "Rheinland-Pfalz", "Saarland", "Sachsen"]

land_arr = ["Germany", "Deutschland"]

context_arr = ["lockdown", "covid", "corona"]

def search_data(kw_array, text):
    '''
    Iterates over an array of keywords and checks for each keyword if its present
    @param kw_array - the array of keywords to search for
    @param text - the text to search in
    @return - true: at least 1 of the keywords is in the text
            - false: none of the keywords are in the text
    '''
    for entry in kw_array:
        if re.search(entry, str(text), re.IGNORECASE):
            return True

    return False



for line in sys.stdin:

    try:

        items = json.loads(line)
        # ["created_at"]
        # ["id"]
        # ["text"]
        # ["user"]["location"]
        # ["user"]["id"]
        # ["geo"]
        # ["entities"]["hashtags"][<index>]["text"]
        # ["lang"]

        location = items["user"]['location']
        location= location.encode('utf-8')
        text = items["text"]
        text = text.encode('utf-8')
        time = datetime.datetime.strptime(items["created_at"], "%a %b %d %H:%M:%S +0000 %Y")
        tweet_id = items["id"]

        # folgende annahmen werden getroffen:
        #    - ein Bundesland kann nur dann richtig erkannt werden wenn es
        #      ausgeschrieben wurde, "MV" als Abkürzung für Mecklenburg Vorpommern
        #      könnte Beispielsweise auch in einem anderen Kontext vorkommen
        #    - Länder analog "DE" für Deutschland könnte auch für etwas anderes stehen
        # check if user has specified a city in the set of the 20 most populated german cities
        #
        # if search_data(city_arr, location) | search_data(land_arr, location) | search_data(bland_arr, location):
        #     if search_data(context_arr, text):
        #     print("%s\t%s\t%s\t%s\t%s" %  (time.date(), 1, tweet_id, time.time(), text))


        print("%s\t%s\t%s\t%s\t%s" %  (time.date(), 1, tweet_id, time.time(), text))


    except (KeyError, AttributeError, ValueError):
        pass
