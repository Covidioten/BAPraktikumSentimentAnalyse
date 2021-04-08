#!/usr/bin/env python3

import sys
from textblob_de import TextBlobDE as TextBlob
import nltk

avg_daily_sent = 0.0
#
# def calcAvg():
#     if adj_tweet < 1:
#         avg_daily_sent = daily_senti_sum / (adj_tweet + 1)
#         # print('avg daily sum ' + str(avg_daily_sent))
#     else:
#         avg_daily_sent = daily_senti_sum / float(adj_tweet)
#         # print('avg daily sum ' + str(avg_daily_sent))

(last_date, sum) = (None, 0)

# stores the amout of tweets with a sentiment score
adj_tweet = 0

# stores the json string for an individual tweet
sum_string = ""

# stores the combined sentiment of all tweets for a day
daily_senti_sum = 0

# main loop - iterates over every line the tokenmapper provides
for line in sys.stdin:
    try:
        (date, val, id, time, text) = line.strip().split("\t")
        senti = TextBlob(text)

        #checks if the entire group for a certain date has been iterated over and a new date group begins
        if last_date and last_date != date:
            # edge case where there is only a single tweet with a sentiment score to avoid dividing by zero
            # calculate the average sentiment for a day
            if adj_tweet < 1:
                avg_daily_sent = daily_senti_sum / (adj_tweet + 1)
            else:
                avg_daily_sent = daily_senti_sum / float(adj_tweet)
                
            
            # generates the final json string for a day
            print( '{"%s":{"date":"%s", "total":"%s", "adj_post": "%s",  "sentiment":"%s", "data":{ %s}}},' % (last_date, last_date, sum, last_date, adj_tweet, round(avg_daily_sent,3), sum_string))

            # reset daily_sentiment_sum
            daily_senti_sum = 0

            # generate the json string that holds the information of a single tweet
            sum_string = "'%s':{'%s':'%s'}" % (id, time, senti.sentiment.polarity)
            (last_date, sum) = (date, int(val))

            # checks if the tweets has a sentiment and inkrements the according variable
            if senti.sentiment.polarity != 0.0:
                adj_tweet += 1

            # sum up daily sentiment
            daily_senti_sum += senti.sentiment.polarity

        # code block to run when iterating over entries of the same day group
        elif last_date:
            # updates the json string, tweet count,  adj_tweet count and polarity
            sum_string += ",'%s':{'%s':'%s'}" % (id, time, senti.sentiment.polarity)
            (last_date, sum) = (date, sum+int(val))
            daily_senti_sum += senti.sentiment.polarity
            if senti.sentiment.polarity != 0.0:
                adj_tweet += 1

        #
        else:
            # updates the json string, tweet count,  adj_tweet count and polarity
            sum_string += "'%s':{'%s':'%s'}" % (id, time, senti.sentiment.polarity)
            (last_date, sum) = (date, sum+int(val))
            daily_senti_sum += senti.sentiment.polarity
            if senti.sentiment.polarity != 0.0:
                adj_tweet += 1

    except ValueError:
        pass

if last_date:
    # edge case where there is only a single tweet with a sentiment score to avoid dividing by zero
    # calculate the average sentiment for a day
    if adj_tweet < 1:
        avg_daily_sent = daily_senti_sum / (float(adj_tweet + 1))
    else:
        avg_daily_sent = daily_senti_sum / float(adj_tweet)

    print( '{"%s":{"date":"%s", "total":"%s", "adj_post":"%s", "sentiment":"%s", "data":{ %s}}},' % (last_date, last_date, sum, adj_tweet, round(avg_daily_sent,3), sum_string))
