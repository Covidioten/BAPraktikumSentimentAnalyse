# -*- coding: utf-8 -*-
from textblob_de import TextBlobDE
import nltk
nltk.download('punkt')


def get_sentiment_of_string(sentence: str) -> float:
    sentence_as_blob = TextBlobDE(sentence)
    return sentence_as_blob.sentiment.polarity
