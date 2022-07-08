<<<<<<< HEAD
import twint
from langdetect import detect
import pandas as pd

initial_date = '2019-08-10'
final_date = '2019-09-30'
keywords = 'once upon a time in hollywood'

#----SEARCH TWEETS-----

c = twint.Config()
c.Since = initial_date
c.Search = keywords
c.Until = final_date
c.Custom["tweet"] = ['tweet']
c.Limit = 500
c.Pandas = True
twint.run.Search(c)

Tweets_df = twint.storage.panda.Tweets_df

#----LANGUAGE DETECTION-----

lang_list = []
for tweet in Tweets_df.tweet:
    lang = detect(tweet)
    lang_list.append(lang)

df = pd.DataFrame({'tweet': Tweets_df.tweet, 'lang': lang_list})
df_es = df.loc[df['lang'] == 'es']
df_en = df.loc[df['lang'] == 'en']

#----EXPORT TO CSV-----

df_es.to_csv(f'{keywords}_ES.csv')
=======
import twint
from langdetect import detect
import pandas as pd

initial_date = '2019-08-10'
final_date = '2019-09-30'
keywords = 'once upon a time in hollywood'

#----SEARCH TWEETS-----

c = twint.Config()
c.Since = initial_date
c.Search = keywords
c.Until = final_date
c.Custom["tweet"] = ['tweet']
c.Limit = 500
c.Pandas = True
twint.run.Search(c)

Tweets_df = twint.storage.panda.Tweets_df

#----LANGUAGE DETECTION-----

lang_list = []
for tweet in Tweets_df.tweet:
    lang = detect(tweet)
    lang_list.append(lang)

df = pd.DataFrame({'tweet': Tweets_df.tweet, 'lang': lang_list})
df_es = df.loc[df['lang'] == 'es']
df_en = df.loc[df['lang'] == 'en']

#----EXPORT TO CSV-----

df_es.to_csv(f'{keywords}_ES.csv')
>>>>>>> 01dfa172072e1852cec24e52872916c7c47f9f89
df_en.to_csv(f'{keywords}_EN.csv')