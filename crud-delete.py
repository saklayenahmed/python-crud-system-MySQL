import mysql.connector as sql

# connect mysql
connect = sql.connect(host="localhost", user="root", passwd="", database="python")
conn = connect.cursor()

deleteId = input("Enter Name for delete: ")
conn.execute("select * from info where name=%s", [deleteId])
info = conn.fetchall()
row = conn.rowcount
if row > 0:
    print(info)
    inputName = input("Do you want to delete? Type YES/NO: ")
    inputName = inputName.replace("Do you want to delete? Type YES/NO: ", '')
    if inputName == "YES":
        conn.execute("DELETE FROM info WHERE name=%s", [deleteId])
        connect.commit()
        print('Deleted Succesfully.')
    else:
        print("Application closed by user.")
        quit()
else:
    print("No Data Found.")

