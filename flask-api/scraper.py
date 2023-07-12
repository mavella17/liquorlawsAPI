from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import pprint
import sqlalchemy as db
from sqlalchemy import select
from sqlalchemy.sql import text as sa_text


#   verify status code
engine = db.create_engine('sqlite:///laws.db')
url = "https://en.wikipedia.org/wiki/List_of_alcohol_laws_of_the_United_States"
table_class ="wikitable"
response = requests.get(url)
print(response.status_code)

# parse HTML
soup = bs(response.content, 'html.parser')
table = soup.find_all('table', {'class': "wikitable"})

# compile 5 tables from wikipedia
dfs = []
for t in table:
    df = pd.read_html(str(t))[0]
    df.columns = df.columns.map(': '.join)
    df.rename(columns={'State federal district  or territory: State federal district  or territory':'Location'}, inplace=True)
    df.rename(columns={'Notes: Notes': 'Notes'}, inplace=True)
    dfs.append(df)
combined_df = pd.concat(dfs,axis=0)
states = [ 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA',
           'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA',
           'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
           'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'PR']
combined_df.insert(1,'Abbreviation',states)
pprint.pprint(combined_df.columns.tolist())
#print("Resulting DB: \n --------- \n",combined_df)
#print(combined_df.columns)
combined_df.to_sql('laws', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
    query_result = connection.execute(db.text("""SELECT * FROM
    laws where Abbreviation = 'AK'""")).fetchall()
    #print("Getting DB: \n --------- \n",pd.DataFrame(query_result))
