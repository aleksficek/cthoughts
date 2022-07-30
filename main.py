from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')

import praw

reddit = praw.Reddit(client_id='44iWCFZcG-EY3287Dcb57A',
                     client_secret='EEXITDZXLAvhtXBZK6KRyIVubyDqYA',
                     user_agent='aficek')

headlines = set()

for submission in reddit.subreddit('covidlonghaulers').new(limit=None):
    headlines.add(submission.title)
    display.clear_output()
    print(len(headlines))


from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

pprint(results[:3], width=100)