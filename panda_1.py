import pandas as pd

pkm_data = pd.read_csv("pokemon_data.csv")

# pkm_data_xlsx = pd.read_excel("pokemon_data.xlsx").head(20)

# pkm_data_txt = pd.read_csv("pokemon_data.txt", delimiter='\t').tail(20)

# read the name column from 0 to 77 but show on the last 10 in this selection
print(pkm_data['Name'][0:77].tail(10))

# read the specified columns but only show the first 15
print(pkm_data[['Name', 'Type 1', 'HP']].head(15))

# read each row
print(pkm_data.iloc[1]) # integer location, reads only row 1
print(pkm_data.iloc[1:100:4].tail(5)) # reads every fourth row, from 1 to 100, print last 5 entries
