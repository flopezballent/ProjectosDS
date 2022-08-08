import snscrape.modules.twitter as sntwitter
import pandas as pd
from langdetect import detect

# Creando la lista donde se almacenaron los Tweets  de la keyword a buscar.
tweets_list = []
keywords = 'TopGunMaverick'

# Usando TwitterSearchScraper para hacer scrape data y agregar tweets a la lista
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keywords} since:2022-05-25 until:2022-05-27').get_items()):
    if i>11700:
        break
    tweets_list.append([tweet.date, tweet.content, tweet.user])
    
# Creando el DataFrame con la lista de tweets 
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