#!/usr/bin/env python
import sys
from textblob_de import TextBlobDE as TextBlob
import nltk
nltk.download('punkt')
avg_daily_sent = 0.0

def calcAvg():
    if adj_tweet < 1:
        avg_daily_sent = daily_senti_sum / (float(adj_tweet + 1))
        print('avg daily sum ' + str(avg_daily_sent))
    else:
        avg_daily_sent = daily_senti_sum / float(adj_tweet)
        print('avg daily sum ' + str(avg_daily_sent))

(last_date, sum) = (None, 0)
#adjusted daily senti
adj_tweet = 0

temp_string = ""
counter = 0
(last_id, last_time, last_text, last_senti, last_avg_senti) = (0, None, None, None, None)
sum_string = ""
daily_senti_sum = 0
print("{'root':[")

for line in sys.stdin:
    try:
        (id, date, val, time, text) = line.strip().split("\t")
        senti = TextBlob(text)
        avg_senti = TextBlob(text)

        if last_date and last_date != date:
            if adj_tweet < 1:
                avg_daily_sent = daily_senti_sum / (float(adj_tweet + 1))
                print('avg daily sum ' + str(avg_daily_sent))
            else:
                avg_daily_sent = daily_senti_sum / float(adj_tweet)
                print('avg daily sum ' + str(avg_daily_sent))
            print( "{'%s':{'total':'%s', 'adj_post': '%s',  'sentiment':'%s', 'data':{ %s}}}," % (last_date, sum, adj_tweet, avg_daily_sent, sum_string))
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
            # (last_id, last_time, last_senti, sum_string) = (id, time, senti, )
        else:
            sum_string += "'%s':{'%s':'%s'}" % (id, time, senti.sentiment.polarity)
            (last_date, sum) = (date, sum+int(val))
            daily_senti_sum += senti.sentiment.polarity
            if senti.sentiment.polarity != 0.0:
                adj_tweet += 1
            # (last_id, last_time, last_senti, sum_string) = (id, time, senti, )
    except ValueError:
        pass

if last_date:
    if adj_tweet < 1:
        avg_daily_sent = daily_senti_sum / (float(adj_tweet + 1))
        print('avg daily sum ' + str(avg_daily_sent))
    else:
        avg_daily_sent = daily_senti_sum / float(adj_tweet)
        print('avg daily sum ' + str(avg_daily_sent))
    print('lol: ' + str(avg_daily_sent))
    print( "{'%s':{'total':'%s', 'adj_post': '%s', 'sentiment':'%f', 'data':{ %s}}}" % (last_date, sum, adj_tweet, float(avg_daily_sent), sum_string))
    print('adj_tweet:' + str(adj_tweet))
    # print("}}")
    print("]}")
    print("daily_sum: " + str(daily_senti_sum))
    print("adj_tweet: "+ str(adj_tweet))
