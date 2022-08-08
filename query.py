import pandas as pd

dataset = pd.read_csv('IMDB Dataset.csv')
dataset.to_sql('imdb_db.sql')
