import mysql.connector as sql

# connect mysql
connect = sql.connect(host="localhost", user="root", passwd="", database="python")
conn = connect.cursor()

updateId = input("Enter Name for update: ")
conn.execute("select * from info where name=%s", [updateId])
info = conn.fetchall()
row = conn.rowcount
if row > 0:
    print(info)
    inputName = input("Update Name: ")
    inputMobile = input("Update Mobile: ")
    inputName = input("Do you want to delete? Type YES/NO: ")
    inputName = inputName.replace("Do you want to delete? Type YES/NO: ", '')
    if inputName == "YES":
        conn.execute("UPDATE info SET name=%s, mobile=%s WHERE name=%s",[inputName, inputMobile, updateId])
        connect.commit()
        print('Updated Succesfully.')
    else:
        print("Application closed by user.")
        quit()
else:
    print("No Data Found.")
