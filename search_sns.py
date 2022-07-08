<<<<<<< HEAD
import os

initial_date = '2022-05-29'
final_date = '2022-06-25'
keywords = 'lightyear'

# Using OS library to call CLI commands in Python
os.system(f'snscrape --jsonl --max-results 500 --since {initial_date} twitter-search \"{keywords} until:{final_date}\" > {keywords}_sns.json')
=======
import os

initial_date = '2022-05-29'
final_date = '2022-06-25'
keywords = 'lightyear'

# Using OS library to call CLI commands in Python
os.system(f'snscrape --jsonl --max-results 500 --since {initial_date} twitter-search \"{keywords} until:{final_date}\" > {keywords}_sns.json')

>>>>>>> 01dfa172072e1852cec24e52872916c7c47f9f89
