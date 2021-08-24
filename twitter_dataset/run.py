# Copyright 2021 BISITE Research Group
# See LICENSE for details.
#!usr/bin/python

# Copyright 2021 BISITE Research Group
# See LICENSE for details.
import sys
import twint
import datetime
import time
import json
import io

def create_tweets_dataset(keywords: str):
    """
    Get tweets and save it into CSV format
    Args:
        keywords(:obj:`str`): the topics used for searching tweets

    """
    c = twint.Config()
    c.Limit = 200000
    c.Pandas = True
    c.Lang = "es"
    c.Hide_output = True
    c.Search = keywords
    twint.run.Search(c)
    Tweets_df = twint.storage.panda.Tweets_df
    #Get the relevant information for dataset
    Tweets_df = Tweets_df[["date", "username", "search", "tweet", "language"]]
    #Get just the spanish tweets
    Tweets_df = Tweets_df[Tweets_df['language'].isin(['es'])]
    #Export to CSV
    Tweets_df.to_csv(
        header=["Date", "Username", "Search", "Tweet", "language"],
        path_or_buf='Tweets_dataset.csv',
        sep=',',
        index=False)

def main():
    #Keywords for the topics search, needed to add OR between words
    try:
        keywords = sys.argv[1].replace(',',' OR ')
        create_tweets_dataset(keywords)
    except:
        print('Es necesario incluir una lista de palabras separadas por \',\'. \nEjemplo: musica,baile')

def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs
if __name__ == '__main__':
    requirements('requirements.txt')
    main()



   
