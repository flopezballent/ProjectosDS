import snscrape.modules.twitter as sntwitter
import pandas as pd
from langdetect import detect

# Creating list to append tweet data to
tweets_list = []
keywords = 'lightyear'

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keywords} since:2022-05-01 until:2022-06-30').get_items()):
    if i>50:
        break
    tweets_list.append([tweet.date, tweet.content, tweet.user])
    
# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text', 'Username'])
print(tweets_df)

#----LANGUAGE DETECTION-----

lang_list = []
for tweet in tweets_df.Text:
    lang = detect(tweet)
    lang_list.append(lang)

df = pd.DataFrame({'tweet': tweets_df.Text, 'lang': lang_list})
df_es = df.loc[df['lang'] == 'es']
df_en = df.loc[df['lang'] == 'en']

#----EXPORT TO CSV-----

df.to_csv(f'{keywords}.csv')
df_es.to_csv(f'{keywords}_ES.csv')
df_en.to_csv(f'{keywords}_EN.csv')