# Welcome to My M And A
In this project, we took 3 customer data and homogenized them into a database file.

## Task
The main challenge in this assignment was data cleaning.

## Description
I cleaned the data and assigned the correct datatypes to them.

## Installation
These functions should be written at the end of the my_m_and_a.py file with proper arguments.
"""
merged_csv = my_m_and_a(io.StringIO('only_wood_customer_us_1.csv'),io.StringIO('only_wood_customer_us_1.csv'),io.StringIO('only_wood_customer_us_1.csv'))
my_ds_babel.csv_to_sql(merged_csv, 'plastic_free_boutique.sql', 'customers')
"""

## Usage
python my_m_and_a.py

### The Core Team

<span><i>Made at <a href='https://qwasar.io'>Qwasar Silicon Valley</a></i></span>
<span><img alt='Qwasar Silicon Valley Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
