#!/usr/bin/env python3

import sys
from textblob_de import TextBlobDE as TextBlob
import nltk

avg_daily_sent = 0.0

def calcAvg():
    if adj_tweet < 1:
        avg_daily_sent = daily_senti_sum / (adj_tweet + 1)
        # print('avg daily sum ' + str(avg_daily_sent))
    else:
        avg_daily_sent = daily_senti_sum / float(adj_tweet)
        # print('avg daily sum ' + str(avg_daily_sent))

(last_date, sum) = (None, 0)
#adjusted daily senti
adj_tweet = 0

sum_string = ""
daily_senti_sum = 0
# print("{'root':[")

for line in sys.stdin:
    try:
        (date, val, id, time, text) = line.strip().split("\t")
        senti = TextBlob(text)

        if last_date and last_date != date:
            if adj_tweet < 1:
                avg_daily_sent = daily_senti_sum / (adj_tweet + 1)

            else:
                avg_daily_sent = daily_senti_sum / float(adj_tweet)
                # print('avg daily sum ' + str(avg_daily_sent))
            print( "{'%s':{'total':'%s', 'date':'%s', 'adj_post': '%s',  'sentiment':'%s', 'data':{ %s}}}," % (last_date, sum, last_date, adj_tweet, round(avg_daily_sent,3), sum_string))
            daily_senti_sum = 0
            sum_string = "'%s':{'%s':'%s'}" % (id, time, senti.sentiment.polarity)
            (last_date, sum) = (date, int(val))
            if senti.sentiment.polarity != 0.0:
                adj_tweet += 1
            daily_senti_sum += senti.sentiment.polarity

        elif last_date:
            sum_string += ",'%s':{'%s':'%s'}" % (id, time, senti.sentiment.polarity)
            (last_date, sum) = (date, sum+int(val))
            daily_senti_sum += senti.sentiment.polarity
            if senti.sentiment.polarity != 0.0:
                adj_tweet += 1

        else:
            sum_string += "'%s':{'%s':'%s'}" % (id, time, senti.sentiment.polarity)
            (last_date, sum) = (date, sum+int(val))
            daily_senti_sum += senti.sentiment.polarity
            if senti.sentiment.polarity != 0.0:
                adj_tweet += 1

    except ValueError:
        pass

if last_date:
    if adj_tweet < 1:
        avg_daily_sent = daily_senti_sum / (float(adj_tweet + 1))
    else:
        avg_daily_sent = daily_senti_sum / float(adj_tweet)

    print( "{'%s':{'total':'%s', 'adj_post': '%s', 'sentiment':'%s', 'data':{ %s}}}" % (last_date, sum, adj_tweet, round(avg_daily_sent,3), sum_string))
