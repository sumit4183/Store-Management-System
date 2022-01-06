def login(u,p):
    import mysql.connector as con
    db = con.connect(host="localhost", user="root", password="hello!123",database="shop", auth_plugin='mysql_native_password')
    cur = db.cursor()
    cur.execute("select * from login")
    f = cur.fetchall()
    t = dict(f)
    if u in t.keys():
        if p in t.values():
            return 1
    else:
        return 0

def check():
    a = input("Enter your user_id:")
    b = input("Enter your password:")
    c = login(a,b)
    if c==1:
        return 1
        



        
        
    
