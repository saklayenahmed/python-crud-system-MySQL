import mysql.connector as sql

# connect mysql
connect = sql.connect(host="localhost", user="root", passwd="", database="python")
conn = connect.cursor()

conn.execute("select * from info")
info = conn.fetchall()
print(info)



