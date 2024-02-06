# Scraping para verificar se determinados textos existem no HTML de determinadas páginas

## Importa bibliotecas
import requests
import pandas as pd
import os

## Define algumas variáveis importantes
URL_COLUMN = 'url'
QUERY_COLUMN = 'texto'
DATABASE_DIRECTORY = 'entrada'

## Define algumas funções convenientes
def add_df_to_list(df: pd.DataFrame, df_list: list):
    if (URL_COLUMN in df.columns and QUERY_COLUMN in df.columns):
            filtered_df = df[[URL_COLUMN, QUERY_COLUMN]]
            df_list.append(filtered_df)

def generate_df(path: str):
     if path.endswith('.xlsx'):
          return pd.read_excel(path)
     if path.endswith('.csv'):
          return pd.read_csv(path)
     
## Pega os dataframes e gera a lista
files = os.listdir(DATABASE_DIRECTORY)
df_list = []

for file in files:
    path = DATABASE_DIRECTORY + '/' + file
    df = generate_df(path)
    if(type(df) == pd.DataFrame):
        add_df_to_list(df, df_list)

## Percorre a lista verificando se as páginas contem um determinado texto no html
final_list = []
url = ''
response = ''

for df in df_list:
    for index, row in df.iterrows():

        if url != row[URL_COLUMN]:
            url = row[URL_COLUMN]
            response = requests.get(url)
        
        found = False

        if (response.text.find(row[QUERY_COLUMN]) != -1):
            found = True

        final_list.append({
            'url': row[URL_COLUMN],
            'query': row[QUERY_COLUMN],
            'found': found,
            'status_code': response.status_code
        })

final_df = pd.DataFrame(final_list)

## Exporta planilha
final_df.to_excel('saida/saida.xlsx', index=True)