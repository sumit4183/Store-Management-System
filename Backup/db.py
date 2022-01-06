import mysql.connector as con

########## Creating the new database and deletes any old ones ##########
db = con.connect(host="localhost", user="root", password="hello!123")
cur = db.cursor()

cur.execute("drop database if exists shop")
db.commit()

cur.execute("create database shop")
db.commit()

def tables(): #Creating Tables for databases
    import mysql.connector as con
    db = con.connect(host="localhost", user="root", password="hello!123", database="shop")
    cur = db.cursor()
    ##### Creating login table #####
    cur.execute("""create table login
(u_id varchar(10) primary key,
pwd varchar(15) not null)""")
    
    ##### Creating purchase table #####
    cur.execute("""create table purchase
(date date not null,
g_wt float(10,3) not null default 0,
g_rate float(10,2) not null default 0,
g_amt float(10,2) not null default 0,
d_wt float(10,2) not null default 0,
d_rate float(10,2) not null default 0,
d_amt float(10,2) not null default 0,
a_wt float(10,3) not null default 0,
a_rate float(10,2) not null default 0,
a_amt float(10,2) not null default 0)""")
    db.commit()

    ##### Creating gold 18K stock table #####
    cur.execute("""create table g18_stock
(date date not null,
g_wt float(10,3) not null default 0,
a_wt float(10,3) not null default 0,
total float(10,3) not null default 0,
issue float(10,3) not null default 0)""")
    db.commit()

    ##### Creating issue table #####
    cur.execute("""create table issue
(date date not null,
g_wt float(10,3) not null default 0,
d_wt float(10,2) not null default 0)""")
    db.commit()

    ##### Creating manufactured table #####
    cur.execute("""create table manufactured
(date date not null,
g_wt float(10,3) not null default 0,
d_wt float(10,2) not null default 0)""")
    db.commit()

    ##### Creating stock table #####
    cur.execute("""create table stock
(date date not null,
g_wt_m float(10,3) not null default 0,
d_wt_m float(10,2) not null default 0,
g_wt_s float(10,3) not null default 0,
d_wt_s float(10,2) not null default 0)""")
    db.commit()

    ##### Creating customer table #####
    cur.execute("""create table customer
(name varchar(20) not null,
date date not null,
item varchar(15) not null,
g_wt float(10,3) not null default 0,
d_wt float(10,2) not null default 0,
amt float(10,2) not null default 0)""")
    db.commit()
    db.close()

def users(): #Entering login details
    import mysql.connector as con
    db = con.connect(host="localhost", user="root", password="hello!123", database="shop")
    cur = db.cursor()
    ####################
    cur.execute("""insert into login
values
("sumit4183", "sp4183")""")
    db.commit()
    ####################
    cur.execute("""insert into login
values
("varad4180", "vk4180")""")
    db.commit()
    db.close()

tables()
users()
