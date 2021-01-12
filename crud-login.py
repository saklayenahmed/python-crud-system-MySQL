import mysql.connector as sql

# connect mysql
connect = sql.connect(host="localhost", user="root", passwd="", database="python")
conn = connect.cursor()

loginId = input("Enter Mobile: ")
conn.execute("select * from info where mobile=%s", [loginId])
info = conn.fetchall()
row = conn.rowcount
if row == 1:
    # print(info)
    print('Loggedin Succesfully.')
    for item in info:
        name = item[1]
        print(f"Welcome {name} to my system.")
    logout = input("Type NO/YES to Logout: ")
    logout = logout.replace("Type NO/YES to Logout: ", '')
    if logout == 'YES':
        print("Loggedout successfully.")
        quit()
else:
    print("Invalid Login Data.")
