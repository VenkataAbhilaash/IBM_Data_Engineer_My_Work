import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db');
table_name= 'instructor'
attribute_list=['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

file_path = 'INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

df.to_sql(table_name,conn,if_exists='replace',index=False)
print("table is ready.")

print(pd.read_sql("SELECT * FROM instructor",conn))

data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')