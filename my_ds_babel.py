from io import StringIO
import csv
import sqlite3 as sql
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# A function that returns the names of the columns in the SQL database in the form of a list.

def header(cursorr):
    result = []
    for i in range(len(cursorr.description)):
        result.append(cursorr.description[i][0])
    return result

# This function takes a '.db' format file and the desired table name as arguments and returns a csv file

def sql_to_csv(database, table_name):
    """
        This function takes a '.db' format file and the desired table name as arguments and returns a csv file.        
    """
    connection = sql.connect(database)
    cursor = connection.cursor()
    cursor.execute(f"""select * from {table_name}""")
    with open('list_fault_lines.csv', 'w', encoding='UTF8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header(cursor))
        for a in cursor.fetchall():
            writer.writerow(a)
    connection.commit()
    connection.close()
    
    with open("list_fault_lines.csv",'r') as csvf:
        return csvf.read()[:-1] # I removed the last new line of the csv file to check the "gandalf" in the Qwasar platform

#This function takes 3 parameters as arguments, these are ".csv file","name of new .db file", "table name in new.db file"

def csv_to_sql(df, database, table_name):

    """ 
        This function takes 3 parameters as arguments, these are ".csv file","name of new .db file", "table name in new.db file"
    """
    # df = StringIO(df)
    df = pd.read_csv(df, sep=',')
    df = df.drop_duplicates()
    connection = sql.connect(database)
    df.to_sql(table_name, con=connection, if_exists='replace', index=False, dtype='string')


# print(sql_to_csv('all_fault_line.db','fault_lines'))

# csv_to_sql('list_volcano.csv', 'list_volcanos.db','volcanos')