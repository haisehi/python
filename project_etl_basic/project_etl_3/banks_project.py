# Code for ETL operations on Country-GDP data

# Importing the required libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
from datetime import datetime
import sqlite3

url = 'https://web.archive.org/web/20230908091635%20/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
db_name = 'Banks.db'
table_name = 'Largest_banks'
output_path = './Largest_banks_data.csv'
csv_path ='exchange_rate.csv'

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("./etl_project_log.txt","a") as f:
        f.write(timestamp + ' : ' + message + '\n')


def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''

    # Implement your code here to extract data from the provided URL
    page = requests.get(url).text
    data = BeautifulSoup(page,'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col) >=3:  # Ensure at least 3 columns exist
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {"Name": col[0].a.contents[0],
                             "MC_USD_Billion": col[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    return df


# Inside the transform() function
def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    # Read the exchange rate CSV file and convert to dictionary
    exchange_rates = pd.read_csv(csv_path)

    # Add columns for Market Cap in GBP, EUR, and INR
    df['MC_GBP_Billion'] = [np.round(x * exchange_rates['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rates['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * exchange_rates['INR'], 2) for x in df['MC_USD_Billion']]

    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_queries(query_statement, sql_connection):
    ''' This function runs the given query statement on the database
    and prints the output along with the query statement. Function returns nothing. '''
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

# Execute 3 function calls using the queries
query_statements = [
    f"SELECT * FROM {table_name}",
    f"SELECT AVG(MC_GBP_Billion) FROM {table_name}",
    f"SELECT Name FROM {table_name} LIMIT 5"
]

''' Here, you define the required entities and call the relevant functions in the correct order to complete the project. 
Note that this portion is not inside any function.'''
log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)
log_progress("Data extraction complete. Initiating Transformation process")

transformed_df = transform(df, csv_path)
log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, csv_path)
log_progress('Data saved to CSV file')

# Initiate SQLite3 connection
sql_connection = sqlite3.connect(db_name)
log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Running the query')

for query in query_statements:
    run_queries(query, sql_connection)

log_progress('Process Complete.')

sql_connection.close()
