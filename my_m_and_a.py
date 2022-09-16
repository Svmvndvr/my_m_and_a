import pandas as pd
import sqlite3
import my_ds_babel
import io


def cleaned_df1(file):
    file_1 = pd.read_csv(file, sep=',')
    print(file_1)
    file_1['Gender'] = file_1['Gender'].replace({'1':'Female','0':'Male','F':'Female','M':"Male"})
    file_1['FirstName'] = file_1['FirstName'].replace({'\W': ''},regex=True).str.title()
    file_1['LastName'] = file_1['LastName'].replace({'\W': ''}, regex=True).str.title()
    file_1['Email'] = file_1['Email'].str.lower()
    file_1['City'] = file_1['City'].replace({'-':' ','_':' '},regex=True).str.title()
    file_1['Country'] = 'USA'
    del file_1['UserName']
    return file_1

def cleaned_df2(file):
    file_2 = pd.read_csv(file, sep=";", names=['Age','City','Gender','Name','Email'])
    file_2['Age'] = file_2['Age'].replace('\D','', regex=True)
    file_2['City'] = file_2['City'].replace({'-':'','_':' '}, regex=True).str.title()
    file_2['Gender'] = file_2['Gender'].replace({'0':'Female','1':'Male','F':'Female','M':"Male"})
    file_2['Name'] = file_2['Name'].replace('[^\w^ ]', '', regex=True).str.title()
    file_2b = file_2['Name'].str.split(expand=True)
    file_2 = file_2.rename(columns={'Name':'Country'})
    file_2['Country'] = 'USA'
    file_2['FirstName'], file_2['LastName'] = file_2b[0],file_2b[1]
    file_2['Email'] = file_2['Email'].str.lower()
    return file_2

def cleaned_df3(file):
    file_3 = pd.read_csv(file, sep=',|\t', engine='python')
    file_3 = file_3.replace({'string_':'','integer_':'','boolean_':'','character_':''}, regex=True)
    file_3['Gender'] = file_3['Gender'].replace({'1': 'Male', '0':'Female', 'M':'Male', 'F':'Female'})
    file_3['Name'] = file_3['Name'].replace('[^\w^ ]', '', regex=True).str.title()
    file_3c = file_3['Name'].str.split(expand=True)
    file_3['FirstName'], file_3['LastName'] = file_3c[0],file_3c[1]
    file_3['Email'] = file_3['Email'].str.lower()
    del file_3['Name']
    file_3['City'] = file_3['City'].replace({'-':'','_':' '}, regex=True).str.title()
    file_3['Age'] = file_3['Age'].replace('\D','', regex=True)
    file_3['Country'] = 'USA'
    return file_3


def my_m_and_a(data1,data2,data3):
    file_1 = cleaned_df1(data1)
    file_2 = cleaned_df2(data2)
    file_3 = cleaned_df3(data3)
    df = pd.concat([file_1,file_2,file_3], ignore_index=True)
    df = df[['Gender', 'FirstName', 'LastName', 'Email', 'Age', 'City', 'Country']]

    df['FirstName'] = df['FirstName'].astype("str")
    df['LastName'] = df['LastName'].astype("str")
    df['Age'] = df['Age'].astype("string")
    return df



""" Uncomment these lines to test these functions with csv content. """

# merged_csv = my_m_and_a('only_wood_customer_us_1.csv','only_wood_customer_us_1.csv','only_wood_customer_us_1.csv')
# my_ds_babel.csv_to_sql(merged_csv, 'plastic_free_boutique.sql', 'customers')



 
