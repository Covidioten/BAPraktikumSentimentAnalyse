#!/usr/bin/env python
import sys
from textblob_de import TextBlobDE as TextBlob
import nltk
nltk.download('punkt')
nltk.data.path.append("../nltk_data/tokenizers/")


(last_date, sum) = (None, 0)
temp_string = ""
counter = 0
(last_id, last_time, last_text, last_senti, last_avg_senti) = (0, None, None, None, None)
sum_string = ""
print("{'root':[")

for line in sys.stdin:
    try:
        (id, date, val, time, text) = line.strip().split("\t")
        senti = TextBlob(text)
        avg_senti = TextBlob(text)



        if last_date and last_date != date:
            print( "{'%s':{'total':'%s', 'sentiment':'%s', 'data':{ %s}}}," % (last_date, sum, avg_senti.sentiment.polarity, sum_string))
            sum_string = "'%s':{'%s':'%s'}" % (id, time, senti.sentiment.polarity)
            (last_date, sum) = (date, int(val))

        elif last_date:
            sum_string += ",'%s':{'%s':'%s'}" % (id, time, senti.sentiment.polarity)
            (last_date, sum) = (date, sum+int(val))
            # (last_id, last_time, last_senti, sum_string) = (id, time, senti, )
        else:
            sum_string += "'%s':{'%s':'%s'}" % (id, time, senti.sentiment.polarity)
            (last_date, sum) = (date, sum+int(val))
            # (last_id, last_time, last_senti, sum_string) = (id, time, senti, )
    except ValueError:
        pass

if last_date:
    print( "{'%s':{'total':'%s', 'sentiment':'%s', 'data':{ %s}}}" % (last_date, sum, avg_senti.sentiment.polarity, sum_string))
    # print("}}")
    print("]}")
