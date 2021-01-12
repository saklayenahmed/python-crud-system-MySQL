import mysql.connector as sql

# connect mysql
connect = sql.connect(host="localhost", user="root", passwd="", database="python")
conn = connect.cursor()

inputName = input("Add Name: ")
inputMobile = input("Add Mobile: ")

conn.execute("INSERT INTO info (name, mobile) VALUES (%s, %s)", [inputName, inputMobile])
connect.commit()
print('Added Succesfully.')
