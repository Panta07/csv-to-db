import csv
import mysql.connector
import time
import datetime

config = {
  'user': 'root',
  'password': '1234',
  'host': '127.0.0.1',
  'database': 'OrganizationsDB',
  'raise_on_warnings': True
}

mydb = mysql.connector.connect(**config)
mycursor = mydb.cursor()
print(mydb) 

def read_rows_from_csv(file_name):
    with open (file_name, "r") as f:
        reader =  csv.DictReader(f)
        for row in reader:
            yield row
            
def insert_row_into_db(row):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    sql_insert_organization = """INSERT INTO Organizations
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
             
    sql_insert_employee = """INSERT INTO Employees
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    # TODO check is there any organization with this ID
    sql_select_organization = f"SELECT OrganizationID FROM Organizations WHERE OrganizationID = {row['Organization Id']}"
    mycursor.execute(sql_select_organization)
    
    result = None 
    for org in mycursor.fetchall():
        result = org
    
    if result is None:
        mycursor.execute(sql_insert_organization, (row['Organization Id'], row['Name'], row['Website'], row['Country'], row['Description'], row['Founded'], row['Industry'], timestamp))
    
    mycursor.execute(sql_insert_employee, (row['ID'], row['Organization Id'], row['First Name'], row['Last Name'], row['Sex'], row['Email'], row['Phone'], row['Date of birth'], row['Job Title'], timestamp))
    mydb.commit()
    # except:
    #     print("exepc")
    #     mydb.rollback()
   
for row in read_rows_from_csv("data.csv"):
    insert_row_into_db(row)
    
mydb.close()