import csv
import mysql.connector as con
import matplotlib.pyplot as pt
from datetime import datetime as date
from tabulate import tabulate
cur=date.now()
dt=cur.strftime("%Y-%m-%d")
####################################################################################################
####################################################################################################
def menu():
    print("""\n1. Purchase\n2. Raw Material\n3. Issued data\n4. Manufactured data\n5. Stock\n6. Customer Data
7. Delete\n8. Backup Data\n9. Restore Data\n10. Exit""")
    a = input("What do you want to view or update?")
    if a=="1":
        purchase()
    elif a=="2":
        raw()
    elif a=="3":
        issue()
    elif a=="4":
        manufactured()
    elif a=="5":
        stock()
    elif a=="6":
        customer()
    elif a=="7":
        delete()
    elif a=="8":
        backup()
    elif a=="9":
        restore()
    elif a=="10":
        print("\nUPDATE SUCCESSFUL")
    else:
        print("\nINVALID INPUT")
        input("Press enter key to return to menu")
        menu()
####################################################################################################
#1.For purcahse data
def purchase():
    import mysql.connector as con
    db = con.connect(host="localhost", user="root", password="hello!123",database="shop")
    cur = db.cursor()
    print("\nYou've chosen 1,")
    a = input("Press\nv to view purchase data\na to add purchase data\nm to return to menu\n")
    ##### Viewing Data #####
    if a=="v" or a=="V":
        ##### Table #####
        cur.execute("Select * from purchase")
        f = cur.fetchall()
        h =["Date","Gold\nWt","Gold\nRate","Gold\nAmount","Diamond\nWt","Diamond\nRate","Diamond\nAmount","Alloy\nWt",
"Alloy\nRate","Alloy\nAmount"]
        tb = tabulate(f, headers=h, tablefmt="pretty")
        print("\nYour purchase data\n",tb)
        ##### Gold Balance(24K) #####
        cur.execute("Select sum(g_wt) from purchase")
        gt = cur.fetchall()
        cur.execute("Select sum(g_wt) from g18_stock")
        gi = cur.fetchall()
        gt = gt[0][0]
        gi = gi[0][0]
        if gt == None and gi == None:
            print("\nNo balance of Gold")
        elif gi == None:
            print("\nTotal gold balance is:",gt)
        else:
            print("\nTotal gold balance is:",gt - gi)
        ##### Diamond Balance #####
        cur.execute("Select sum(d_wt) from purchase")
        dat = cur.fetchall()
        cur.execute("Select sum(d_wt) from issue")
        di = cur.fetchall()
        dat = dat[0][0]
        di = di[0][0]
        if dat == None and di == None:
            print("\nNo balance of Diamond")
        elif di == None:
            print("\nTotal diamond balance is:",dat)
        else:
            print("\nTotal diamond balance is:",dat - di)
        ##### Alloy Balance #####
        cur.execute("Select sum(a_wt) from purchase")
        at = cur.fetchall()
        cur.execute("Select sum(a_wt) from g18_stock")
        ai = cur.fetchall()
        at = at[0][0]
        ai = ai[0][0]
        if at == None and ai == None:
            print("\nNo balance of Alloy")
        elif ai == None:
            print("\nTotal alloy balance is:",at)
        else:
            print("\nTotal alloy balance is:",at - ai)
        input("\nPress enter key to redirect to purchase menu")
        purchase()
    ##### Adding Data #####
    elif a=="a" or a=="A":
        edate=dt
        gw=float(input("Enter gold weight(in gm):"))
        gr=float(input("Enter gold rate(per gm):"))
        dw=float(input("Enter diamond weight(in carat):"))
        dr=float(input("Enter diamond rate(per carat):"))
        aw=float(input("Enter alloy weight(in gm):"))
        ar=float(input("Enter alloy rate(per gm):"))
        ga=gw*gr
        da=dw*dr
        aa=aw*ar
        i="""insert into purchase
(date,g_wt,g_rate,g_amt,d_wt,d_rate,d_amt,a_wt,a_rate,a_amt)
values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cur.execute(i,(edate,gw,gr,ga,dw,dr,da,aw,ar,aa))
        db.commit()
        db.close()
        print("\nENTRY SUCCESSFUL")
        input("\nPress enter key to redirect to purchase menu")
        purchase()
    ##### Returning to Menu #####
    elif a=="m" or a=="M":
        menu()
    ##########
    else:
        print("\nInvalid input")
        input("Press enter key to return to purchase menu")
        purchase()
####################################################################################################
#2.For raw material data
def raw():
    import mysql.connector as con
    db = con.connect(host="localhost", user="root", password="hello!123",database="shop")
    cur = db.cursor()
    print("\nYou've chosen 2,")
    a = input("Press\nv to view raw stock data\na to add 18K gold stock data\nm to return to menu\n")
    ##### Viewing Data #####
    if a=="v" or a=="V":
        ##### Table for 18K Gold Stock ######
        cur.execute("Select * from g18_stock")
        f = cur.fetchall()
        h = ["DATE","Gold\nWt","Alloy\nWt","Total","Issue"]
        tb=tabulate (f, headers=h ,tablefmt="pretty")
        print("\nYour 18K gold stock data is\n",tb)
        ##### 18K Gold Balance #####
        cur.execute("Select sum(total) from g18_stock")
        t = cur.fetchall()
        cur.execute("Select sum(issue) from g18_stock")
        gi = cur.fetchall()
        t = t[0][0]
        gi = gi[0][0]
        if t == None and gi == None:
            print("\nNo balance of 18K Gold")
        elif gi == None:
            print("\nYour 18K gold balance is:",t)
        else:
            print("\nYour 18K gold balance is:",t - gi)
        input("\nPress enter key to redirect to raw stock menu")
        raw()
    ##### Add 18K Gold Stock #####
    elif a=="a" or a=="A":
        edate=dt
        gw=float(input("Enter gold weight:"))
        aw=float(input("Enter alloy weight:"))
        total = aw + gw
        i="Insert into g18_stock(date,g_wt,a_wt,total) values(%s,%s,%s,%s)"
        cur.execute(i,(edate,gw,aw,total))
        db.commit()
        db.close()
        print("\nENTRY SUCCESSFUL")
        input("\nPress enter key to redirect to raw stock menu")
        raw()
    ##### Returning to Menu #####
    elif a=="m" or a=="M":
        menu()
    ##########
    else:
        print("\nInvalid input")
        input("Press enter key to return to manufactured menu")
        manufactured()
####################################################################################################
#3.For gold and diamond issue to the labour
def issue():
    import mysql.connector as con
    db = con.connect(host="localhost", user="root", password="hello!123",database="shop")
    cur = db.cursor()
    print("\nYou've chosen 3,")
    a = input("Press\nv to view issued data\na to add issue data\nm to return to menu\n")
    ##### Viewing Data #####
    if a=="v" or a=="V":
        ##### Table #####
        cur.execute("Select * from issue")
        f = cur.fetchall()
        h = ["Date","Gold\nWt","Diamond\nWt"]
        tb=tabulate (f, headers=h ,tablefmt="pretty")
        print("\nYour issue data is\n",tb)
        ##### Gold Balance #####
        cur.execute("Select sum(g_wt) from issue")
        gt = cur.fetchall()
        cur.execute("Select sum(g_wt) from manufactured")
        mt = cur.fetchall()
        gt = gt[0][0]
        mt = mt[0][0]
        if gt == None and mt == None:
            print("\nNo balance of Gold")
        elif mt == None:
            print("\nTotal gold balance is:",gt)
        else:
            print("\nTotal gold balance is:",gt - mt)
        ##### Diamond Balance #####
        cur.execute("Select sum(d_wt) from issue")
        dat = cur.fetchall()
        cur.execute("Select sum(d_wt) from manufactured")
        mt = cur.fetchall()
        dat = dat[0][0]
        mt = mt[0][0]
        if dat == None and mt == None:
            print("\nNo balance of Diamond")
        elif mt == None:
            print("\nTotal diamond balance is:",dat)
        else:
            print("\nTotal diamond balance is:",dat - mt)
        input("\nPress enter key to redirect to issue menu")
        issue()
    ##### Adding Data #####
    elif a=="a" or a=="A":
        edate=dt
        gw=float(input("Enter gold weight:"))
        dw=float(input("Enter diamond weight:"))
        ##### Entering Data into issue table #####
        i="insert into issue(date,g_wt,d_wt) values(%s,%s,%s)"
        cur.execute(i,(edate,gw,dw))
        ##### Entering data into g18_stock table #####
        i="update g18_stock set issue=%s where date=%s"
        cur.execute(i,(gw,edate))
        db.commit()
        db.close()
        print("\nENTRY SUCCESSFUL")
        input("\nPress enter key to redirect to issue menu")
        issue()
    ##### Returning to Menu #####
    elif a=="m" or a=="M":
        menu()
    ##########
    else:
        print("\nInvalid input")
        input("Press enter key to return to issued menu")
        issue()
####################################################################################################
#4.For entering manufactured data
def manufactured():
    import mysql.connector as con
    db = con.connect(host="localhost", user="root", password="hello!123",database="shop")
    cur = db.cursor()
    print("\nYou've chosen 4,")
    a = input("Press\nv to view manufactured data\na to add manufactured data\nm to return to menu\n")
    ##### Viewing Data #####
    if a=="v" or a=="V":
        ##### Table #####
        cur.execute("Select * from manufactured")
        f = cur.fetchall()
        h = ["Date","Gold\nWt","Diamond\nWt"]
        tb=tabulate (f, headers=h ,tablefmt="pretty")
        print("\nYour manufactured data is\n",tb)
        input("\nPress enter key to redirect to manufactured menu")
        manufactured()
    ##### Adding Data #####
    elif a=="a" or a=="A":
        edate=dt
        gw=float(input("Enter gold weight:"))
        dw=float(input("Enter diamond weight:"))
        ##### Adding Data to Manufactured Table #####
        i="insert into manufactured(date,g_wt,d_wt) values(%s,%s,%s)"
        cur.execute(i,(edate,gw,dw))
        ##### Adding Data to Stock Table #####
        i="insert into stock(date,g_wt_m,d_wt_m) values(%s,%s,%s)"
        cur.execute(i,(edate,gw,dw))
        db.commit()
        db.close()
        print("\nENTRY SUCCESSFUL")
        input("\nPress enter key to redirect to manufactured menu")
        manufactured()
    ##### Returning to Menu #####
    elif a=="m" or a=="M":
        menu()
    ##########
    else:
        print("\nInvalid input")
        input("Press enter key to return to manufactured menu")
        manufactured()
####################################################################################################
#5.For viewing stock
def stock():
    import mysql.connector as con
    db = con.connect(host="localhost", user="root", password="hello!123",database="shop")
    cur = db.cursor()
    print("\nYou've chosen 5,")
    a = input("Press\nv to view stock data\np to see pie chart\nm to return to menu\n")
    ##### Viewing Data #####
    if a=="v" or a=="V":
        ##### Table #####
        cur.execute("Select * from stock")
        f = cur.fetchall()
        h = ["Date","Gold Wt\nMFG","Diamond Wt\nMFG","Gold Wt\nSale","Diamond Wt\nSale"]
        tb=tabulate (f, headers=h ,tablefmt="pretty")
        print("\nYour stock data is\n",tb)
        ##### Gold Balance #####
        cur.execute("Select sum(g_wt_m) from stock")
        mt = cur.fetchall()
        cur.execute("Select sum(g_wt_s) from stock")
        st = cur.fetchall()
        mt = mt[0][0]
        st = st[0][0]
        if mt == None and st == None:
            print("\nNo stock of Gold")
        elif st == None:
            print("\nTotal gold stock is:",mt)
        else:
            print("\nTotal gold stock is:",mt - st)
        ##### Diamond Stock #####
        cur.execute("Select sum(d_wt_m) from stock")
        mt = cur.fetchall()
        cur.execute("Select sum(d_wt_s) from stock")
        st = cur.fetchall()
        mt = mt[0][0]
        st = st[0][0]
        if mt == None and st == None:
            print("\nNo stock of Diamond")
        elif st == None:
            print("\nTotal diamond stock is:",mt)
        else:
            print("\nTotal diamond stock is:",mt - st)
        input("\nPress enter key to redirect to stock menu")
        stock()
    ########## Pie Charts for data ##########
    elif a=="p" or a=="P":
        db = con.connect(host="localhost", user="root", password="hello!123",database="shop")
        cur = db.cursor()
        ##### Layout of Charts #####
        fig, axs = pt.subplots(1,3, num="text")
        ##### Pie chart for gold data #####
        cur.execute("Select sum(g_wt) from purchase")
        g24 = cur.fetchall()
        g24 = g24[0][0]
        cur.execute("Select sum(g_wt) from g18_stock")
        ga = cur.fetchall()
        ga = ga[0][0]
        cur.execute("Select sum(total) from g18_stock")
        g18 = cur.fetchall()
        g18 = g18[0][0]
        cur.execute("Select sum(g_wt) from issue")
        gi = cur.fetchall()
        gi = gi[0][0]
        cur.execute("Select sum(g_wt) from manufactured")
        gm = cur.fetchall()
        gm = gm[0][0]
        cur.execute("Select sum(g_wt) from customer")
        gs = cur.fetchall()
        gs = gs[0][0]
        g24b = g24 - ga
        g18b = g18 - gi
        gib = gi - gm
        gmb = gm - gs
        size = [g24b,g18b,gib,gmb,gs]
        labels = ["24K (%s gm)"%(g24b),"18K (%s gm)"%(g18b),"Issued (%s gm)"%(gib),"Manufactured (%s gm)"%(gmb),
"Sold (%s gm)"%(gs)]
        axs[0].pie(size,startangle=90)
        axs[0].set_title("Gold Data")
        axs[0].legend(labels,title="Gold Data",loc="best")
        ##### Pie chart for diamond data #####
        cur.execute("Select sum(d_wt) from purchase")
        d = cur.fetchall()
        d = d[0][0]
        cur.execute("Select sum(d_wt) from issue")
        di = cur.fetchall()
        di = di[0][0]
        cur.execute("Select sum(d_wt) from manufactured")
        dm = cur.fetchall()
        dm = dm[0][0]
        cur.execute("Select sum(d_wt) from customer")
        ds = cur.fetchall()
        ds = ds[0][0]
        db = d - di
        dib = di - dm
        dmb = dm - ds
        size = [db,dib,dmb,ds]
        labels = ["Stock (%s ct)"%(db),"Issued (%s ct)"%(dib),"Manufactured (%s ct)"%(dmb),"Sold (%s ct)"%(ds)]
        axs[1].pie(size,startangle=90)
        axs[1].set_title("Diamond Data")
        axs[1].legend(labels,title="Diamond Data",loc="best")
        ##### Pie chart for alloy data #####
        db = con.connect(host="localhost", user="root", password="hello!123",database="shop")
        cur = db.cursor()
        cur.execute("Select sum(a_wt) from purchase")
        a = cur.fetchall()
        a = a[0][0]
        cur.execute("Select sum(a_wt) from g18_stock")
        ai = cur.fetchall()
        ai = ai[0][0]
        ab = a - ai
        size = [ab,ai]
        labels = ["Pure (%s gm)"%(ab),"Used (%s gm)"%(ai)]
        axs[2].pie(size,startangle=90)
        axs[2].set_title("Alloy Data")
        axs[2].legend(labels,title="Alloy Data",loc="best")
        pt.show()
        input("\nPress enter key to redirect to stock menu")
        stock()
    ##### Returning to Menu #####
    elif a=="m" or a=="M":
        menu()
    ##########
    else:
        print("\nInvalid input")
        input("Press enter key to return to stock menu")
        stock()
####################################################################################################
#6.For customer data
def customer():
    import mysql.connector as con
    db = con.connect(host="localhost", user="root", password="hello!123",database="shop")
    cur = db.cursor()    
    print("\nYou've chosen 6,")
    a = input("Press\nv to view customer data\na to add customer data\nm to return to menu\n")
    ##### Viewing Data #####
    if a=="v" or a=="V":
        ##### Table #####
        cur.execute("Select * from customer")
        f = cur.fetchall()
        h = ["Name","Date","Item","Gold\nWt","Diamond\nWt","Amount"]
        tb=tabulate (f, headers=h ,tablefmt="pretty")
        print("\nYour customer data is\n",tb)
        input("\nPress enter key to redirect to customer menu")
        customer()
    ##### Adding Data #####
    elif a=="a" or a=="A":
        edate=dt
        n=input("Enter customer name:")
        im=input("Enter item name:")
        gw=float(input("Enter gold weight:"))
        dw=float(input("Enter diamond weight:"))
        a=float(input("Enter amount:"))
        ##### Adding Data to Customer Table #####
        i="insert into customer(name,date,item,g_wt,d_wt,amt) values(%s,%s,%s,%s,%s,%s)"
        cur.execute(i,(n,edate,im,gw,dw,a))
        ##### Adding Data to Stock Table #####
        i="update stock set g_wt_s=%s, d_wt_s=%s where date=%s"
        cur.execute(i,(gw,dw,edate))
        db.commit()
        db.close()
        print("\nENTRY SUCCESSFUL")
        input("\nPress enter key to redirect to customer menu")
        customer()
    ##### Returning to Menu #####
    elif a=="m" or a=="M":
        menu()
    ##########
    else:
        print("\nInvalid input")
        input("Press enter key to return to customer menu")
        customer()
####################################################################################################
#7.For deleting data from particular date
def delete():
    import mysql.connector as con
    from datetime import datetime as date
    db = con.connect(host="localhost", user="root", password="hello!123",database="shop")
    cur = db.cursor()
    print("\nYou've chosen 7,")
    a = input("Press\nd for delete menu\nm to return to menu\n")
    ##### For Deleting Data #####
    if a=="d" or a=="D":
        try:
            d = input('Enter a day(DD):')
            m = input('Enter a month(MM):')
            y = input('Enter a year(YYYY):')
            dat = y + m + d
            i1="delete from purchase where date = %s"%(dat)
            i2="delete from g18_stock where date = %s"%(dat)
            i3="delete from issue where date = %s"%(dat)
            i4="delete from manufactured where date = %s"%(dat)
            i5="delete from stock where date = %s"%(dat)
            i6="delete from customer where date = %s"%(dat)
            cur.execute(i1)
            cur.execute(i2)
            cur.execute(i3)
            cur.execute(i4)
            cur.execute(i5)
            cur.execute(i6)
            db.commit()
            db.close()
            print("\nData successfully deleted from date",d+"-"+m+"-"+y,",if exists")
            input("\nPress enter key to redirect to delete menu")
            delete()
        except:
            print("\nNot a valid date")
            input("\nPress enter key to redirect to delete menu")
            delete()
    ##### Returning to Menu #####
    elif a=="m" or a=="M":
        menu()
    ##########
    else:
        print("\nInvalid input")
        input("Press enter key to return to delete menu")
        delete()
####################################################################################################
#8.To Backup Data
def backup():
    import mysql.connector as con
    db = con.connect(host="localhost", user="root", password="hello!123",database="shop")
    cur = db.cursor()
    print("\nYou've chosen 8,")
    a = input("Press\nb to backup data\nm to return to menu\n")
    ##### Backup Data #####
    if a=="b" or a=="B":
        ##### Purchase Data File #####
        f=open("backup\purchase.csv","w",newline="")
        a = csv.writer(f)
        a.writerow(["Date","Gold Wt.","Gold Rate","Gold Amt.","Diamond Wt.","Diamond Rate","Diamond Amt.","Alloy Wt.","Alloy Rate","Alloy Amt."])
        cur.execute("Select * from purchase")
        fa = cur.fetchall()
        a.writerows(fa)
        f.close()
        ##### 18K Gold Data File #####
        f=open("backup\g18_stock.csv","w",newline="")
        a = csv.writer(f)
        a.writerow(["Date","Gold Wt.","Alloy Wt.","Total","Issue"])
        cur.execute("Select * from g18_stock")
        fa = cur.fetchall()
        a.writerows(fa)
        f.close()
        ##### Issue Data File #####
        f=open("backup\issue.csv","w",newline="")
        a = csv.writer(f)
        a.writerow(["Date","Gold Wt.","Diamond Wt."])
        cur.execute("Select * from issue")
        fa = cur.fetchall()
        a.writerows(fa)
        f.close()
        ##### Manufactured Data File #####
        f=open("backup\manufactured.csv","w",newline="")
        a = csv.writer(f)
        a.writerow(["Date","Gold Wt.","Diamond Wt."])
        cur.execute("Select * from manufactured")
        fa = cur.fetchall()
        a.writerows(fa)
        f.close()
        ##### Stock Data File #####
        f=open("backup\stock.csv","w",newline="")
        a = csv.writer(f)
        a.writerow(["Date","Gold Wt. MFG","Diamond Wt. MFG","Gold Wt. Sale","Diamond Wt. Sale"])
        cur.execute("Select * from stock")
        fa = cur.fetchall()
        a.writerows(fa)
        f.close()
        ##### Customer Data File #####
        f=open("backup\customer.csv","w",newline="")
        a = csv.writer(f)
        a.writerow(["Name","Date","Item","Gold Wt.","Diamond Wt.","Amount"])
        cur.execute("Select * from customer")
        fa = cur.fetchall()
        a.writerows(fa)
        f.close()
        print("\nData Backed up")
        input("\nPress enter key to redirect to backup and restore menu")
        backup()
    ##### Returning to menu #####
    elif a=="m" or a=="M":
        menu()
    ##########
    else:
        print("\nInvalid input")
        input("Press enter key to return to backup menu")
        backup()
####################################################################################################
#9.To Restore Data
def restore():
    import mysql.connector as con
    db = con.connect(host="localhost", user="root", password="hello!123",database="shop")
    cur = db.cursor()
    print("\nYou've chosen 9,")
    a = input("Press\nr to restore data\nm to return to menu\n")
    ##### Backup Data #####
    if a=="r" or a=="R":
        ##### Restoring Purchase Data #####
        cur.execute("delete from purchase")
        db.commit()
        f = open("backup/purchase.csv","r")
        r = csv.reader(f)
        l=[]
        for i in r:
            i =tuple(i)
            l.append(i)
        for x in l[1:]:
            i="""insert into purchase
    (date,g_wt,g_rate,g_amt,d_wt,d_rate,d_amt,a_wt,a_rate,a_amt)
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cur.execute(i,(x))
            db.commit()
        f.close()
        ##### Restoring 18K GOld Stock Data #####
        cur.execute("delete from g18_stock")
        db.commit()
        f = open("backup/g18_stock.csv","r")
        r = csv.reader(f)
        l=[]
        for i in r:
            i =tuple(i)
            l.append(i)
        for x in l[1:]:
            i="""Insert into g18_stock
    (date,g_wt,a_wt,total,issue)
    values(%s,%s,%s,%s,%s)"""
            cur.execute(i,(x))
            db.commit()
        f.close()
        ##### Restoring Issued Data #####
        cur.execute("delete from issue")
        db.commit()
        f = open("backup/issue.csv","r")
        r = csv.reader(f)
        l=[]
        for i in r:
            i =tuple(i)
            l.append(i)
        for x in l[1:]:
            i="""Insert into issue
    (date,g_wt,d_wt)
    values(%s,%s,%s)"""
            cur.execute(i,(x))
            db.commit()
        f.close()
        ##### Restoring Manufactured Data #####
        cur.execute("delete from manufactured")
        db.commit()
        f = open("backup/manufactured.csv","r")
        r = csv.reader(f)
        l=[]
        for i in r:
            i =tuple(i)
            l.append(i)
        for x in l[1:]:
            i="""Insert into manufactured
    (date,g_wt,d_wt)
    values(%s,%s,%s)"""
            cur.execute(i,(x))
            db.commit()
        f.close()
        ##### Restoring Stock Data #####
        cur.execute("delete from stock")
        db.commit()
        f = open("backup/stock.csv","r")
        r = csv.reader(f)
        l=[]
        for i in r:
            i =tuple(i)
            l.append(i)
        for x in l[1:]:
            i="""Insert into stock
    (date,g_wt_m,d_wt_m,g_wt_s,d_wt_s)
    values(%s,%s,%s,%s,%s)"""
            cur.execute(i,(x))
            db.commit()
        f.close()
        ##### Restoring Customer Data #####
        cur.execute("delete from customer")
        db.commit()
        f = open("backup/customer.csv","r")
        r = csv.reader(f)
        l=[]
        for i in r:
            i =tuple(i)
            l.append(i)
        for x in l[1:]:
            i="""Insert into customer
    (name,date,item,g_wt,d_wt,amt)
    values(%s,%s,%s,%s,%s,%s)"""
            cur.execute(i,(x))
            db.commit()
        f.close()
        print("\nData Restored")
        input("\nPress enter key to redirect to backup and restore menu")
        restore()
    ##### Returning to menu #####
    elif a=="m" or a=="M":
        menu()
    ##########
    else:
        print("\nInvalid input")
        input("Press enter key to return to restore menu")
        restore()

        

