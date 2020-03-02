###tkinter initialization###############
from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import turtle       
########################################################################
root=Tk()
root.config(bg='lawn green')
root.title("SHOPPING CART")
width = 1024
height = 920
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
TopForm = Frame(root, width=900, height=200, bd=1, relief=SOLID)
TopForm.pack(side=TOP)
lbl_text = Label(TopForm, text='SHOPPING CART NAVIGATION',font=('arial',24,'bold'), width=600,fg='black',bg='snow',relief=RAISED)
lbl_text.pack(fill=X)
#####################################################################################

################################variables##########################################
SEARCH=StringVar()
prodname = StringVar()
pric1 = IntVar()
row1= IntVar()
column1=IntVar()
sec1=StringVar()
prod1name = StringVar()
pric2 = IntVar()
row2 = IntVar()
column2=IntVar()
sec2=StringVar()
prod2name = StringVar()
pric3 = IntVar()
row3 = IntVar()
column3=IntVar()
sec3=StringVar()
prod3name = StringVar()
pric4 = IntVar()
row4 = IntVar()
column4=IntVar()
sec4=StringVar()
prod4name = StringVar()
pric5 = IntVar()
row5 = IntVar()
column5=IntVar()
sec5=StringVar()

######################################################back end database commands######################################
def Database():
    global conn, cursor
    conn = sqlite3.connect("finaleb.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `deli` (prodn1 TEXT, price INTEGER, ROW INTEGER,COLUMN INTEGER,SECTION TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `health` (prodn2 TEXT, price INTEGER,ROW INTEGER,COLUMN INTEGER,SECTION TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `home` (prodn3 TEXT, price INTEGER, ROW INTEGER,COLUMN INTEGER,SECTION TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `dried` (prod4 TEXT, price INTEGER, ROW INTEGER,COLUMN INTEGER,SECTION TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `packed` (prodn5 TEXT, price INTEGER, ROW INTEGER,COLUMN INTEGER,SECTION TEXT)")
    
#########################################################################################################################################################################################

####################################################outgoinhaddview###########################################################################################################################
                
def AddNew10():
        Database()
        cursor.execute("INSERT INTO `deli` (prodn1 , price , ROW ,COLUMN ,SECTION ) VALUES(?,?,?,?,?)", (str(prodname.get()),int(pric1.get()), int(row1.get()), int(column1.get()),str(sec1.get())))
        conn.commit()
        prodname.set("")
        pric1.set("")
        row1.set("")
        column1.set("")
        sec1.set("")
        cursor.close()
        conn.close()

def ShowView10():
    global viewform,Home
    Home=Tk()
    viewform = Toplevel()
    viewform.title("unit window")
    width = 900
    height = 600
    Home.config(bg='lawn green')
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm10()

def ViewForm10():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600,bg='lawn green')
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600,bg='lawn green')
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="DELI", font=('arial', 18),fg='black',bg='snow',relief=RAISED)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15),bg='lawn green')
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search10,fg='black',bg='snow',relief=RAISED)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset10,fg='black',bg='snow',relief=RAISED)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="back", command=DIS,fg='black',bg='snow',relief=RAISED)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="sections_map", command=t1,fg='black',bg='snow',relief=RAISED)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("PRODUCT_NAME","PRODUCT_PRICE","ROW_PLACED", "COLUMN_PLACED","SECTION"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('PRODUCT_NAME', text="PRODUCT_NAME",anchor=W)
    tree.heading('PRODUCT_PRICE', text="PRODUCT_PRICE",anchor=W)
    tree.heading('ROW_PLACED', text="ROW_PLACED",anchor=W)
    tree.heading('COLUMN_PLACED', text="COLUMN_PLACED",anchor=W)
    tree.heading('SECTION', text="SECTION",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.pack()
    DisplayData10()
    
def DisplayData10():
    Database()
    cursor.execute("SELECT * FROM `deli`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search10():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `deli` WHERE `prodn1` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        
        
        
def Reset10():
    tree.delete(*tree.get_children())
    DisplayData10()
    SEARCH.set("")


###############################################################################################################################################################################################################

####################################################outgoinhaddview###########################################################################################################################
                
def AddNew11():
        Database()
        cursor.execute("INSERT INTO `health` (prodn2 , price , ROW ,COLUMN ,SECTION ) VALUES(?,?,?,?,?)", (str(prod1name.get()),int(pric2.get()), int(row2.get()), int(column2.get()),str(sec2.get())))
        conn.commit()
        prod1name.set("")
        pric2.set("")
        row2.set("")
        column2.set("")
        sec2.set("")
        cursor.close()
        conn.close()

def ShowView11():
    global viewform,Home
    Home=Tk()
    viewform = Toplevel()
    viewform.title("unit window")
    width = 900
    height = 600
    Home.config(bg='lawn green')
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm11()

def ViewForm11():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600,bg='lawn green')
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600,bg='lawn green')
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="DELI", font=('arial', 18),fg='black',bg='snow',relief=RAISED)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15),bg='lawn green')
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search11,fg='black',bg='snow',relief=RAISED)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset11,fg='black',bg='snow',relief=RAISED)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="back", command=DIS,fg='black',bg='snow',relief=RAISED)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="sections_map", command=t1,fg='black',bg='snow',relief=RAISED)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("PRODUCT_NAME","PRODUCT_PRICE","ROW_PLACED", "COLUMN_PLACED","SECTION"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('PRODUCT_NAME', text="PRODUCT_NAME",anchor=W)
    tree.heading('PRODUCT_PRICE', text="PRODUCT_PRICE",anchor=W)
    tree.heading('ROW_PLACED', text="ROW_PLACED",anchor=W)
    tree.heading('COLUMN_PLACED', text="COLUMN_PLACED",anchor=W)
    tree.heading('SECTION', text="SECTION",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.pack()
    DisplayData11()
    
def DisplayData11():
    Database()
    cursor.execute("SELECT * FROM `health`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search11():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `health` WHERE `prodn2` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset11():
    tree.delete(*tree.get_children())
    DisplayData11()
    SEARCH.set("")

###############################################################################################################################################################################################################

####################################################outgoinhaddview###########################################################################################################################
                
def AddNew12():
        Database()
        cursor.execute("INSERT INTO `home` (prodn3 , price , ROW ,COLUMN ,SECTION ) VALUES(?,?,?,?,?)", (str(prod2name.get()),int(pric3.get()), int(row3.get()), int(column3.get()),str(sec3.get())))
        conn.commit()
        prod2name.set("")
        pric3.set("")
        row3.set("")
        column3.set("")
        sec3.set("")
        cursor.close()
        conn.close()

def ShowView12():
    global viewform,Home
    Home=Tk()
    viewform = Toplevel()
    viewform.title("unit window")
    width = 900
    height = 600
    Home.config(bg='lawn green')
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm12()

def ViewForm12():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600,bg='lawn green')
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600,bg='lawn green')
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="DELI", font=('arial', 18),fg='black',bg='snow',relief=RAISED)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15),bg='lawn green')
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search12,fg='black',bg='snow',relief=RAISED)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset12,fg='black',bg='snow',relief=RAISED)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="back", command=DIS,fg='black',bg='snow',relief=RAISED)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="sections_map", command=t1,fg='black',bg='snow',relief=RAISED)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("PRODUCT_NAME","PRODUCT_PRICE","ROW_PLACED", "COLUMN_PLACED","SECTION"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('PRODUCT_NAME', text="PRODUCT_NAME",anchor=W)
    tree.heading('PRODUCT_PRICE', text="PRODUCT_PRICE",anchor=W)
    tree.heading('ROW_PLACED', text="ROW_PLACED",anchor=W)
    tree.heading('COLUMN_PLACED', text="COLUMN_PLACED",anchor=W)
    tree.heading('SECTION', text="SECTION",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.pack()
    DisplayData12()
    
def DisplayData12():
    Database()
    cursor.execute("SELECT * FROM `home`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search12():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `home` WHERE `prodn3` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset12():
    tree.delete(*tree.get_children())
    DisplayData12()
    SEARCH.set("")

###############################################################################################################################################################################################################

####################################################outgoinhaddview###########################################################################################################################
                
def AddNew13():
        Database()
        cursor.execute("INSERT INTO `dried` (prod4 , price , ROW ,COLUMN ,SECTION ) VALUES(?,?,?,?,?)", (str(prod3name.get()),int(pric4.get()), str(row4.get()), int(column4.get()),str(sec4.get())))
        conn.commit()
        prod3name.set("")
        pric4.set("")
        row4.set("")
        column4.set("")
        sec4.set("")
        cursor.close()
        conn.close()

def ShowView13():
    global viewform,Home
    Home=Tk()
    viewform = Toplevel()
    viewform.title("unit window")
    width = 900
    height = 600
    Home.config(bg='lawn green')
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm13()

def ViewForm13():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600,bg='lawn green')
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600,bg='lawn green')
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="DELI", font=('arial', 18),fg='black',bg='snow',relief=RAISED)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15),bg='lawn green')
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search13,fg='black',bg='snow',relief=RAISED)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset13,fg='black',bg='snow',relief=RAISED)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="back", command=DIS,fg='black',bg='snow',relief=RAISED)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="sections_map", command=t1,fg='black',bg='snow',relief=RAISED)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("PRODUCT_NAME","PRODUCT_PRICE","ROW_PLACED", "COLUMN_PLACED","SECTION"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('PRODUCT_NAME', text="PRODUCT_NAME",anchor=W)
    tree.heading('PRODUCT_PRICE', text="PRODUCT_PRICE",anchor=W)
    tree.heading('ROW_PLACED', text="ROW_PLACED",anchor=W)
    tree.heading('COLUMN_PLACED', text="COLUMN_PLACED",anchor=W)
    tree.heading('SECTION', text="SECTION",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.pack()
    DisplayData13()
    
def DisplayData13():
    Database()
    cursor.execute("SELECT * FROM `dried`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search13():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `dried` WHERE `prod4` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset13():
    tree.delete(*tree.get_children())
    DisplayData13()
    SEARCH.set("")



###############################################################################################################################################################################################################

####################################################outgoinhaddview###########################################################################################################################
                
def AddNew14():
        Database()
        cursor.execute("INSERT INTO `packed` (prodn5 , price , ROW ,COLUMN ,SECTION ) VALUES(?,?,?,?,?)", (str(prod4name.get()),int(pric5.get()), int(row5.get()), int(column5.get()),str(sec5.get())))
        conn.commit()
        prod4name.set("")
        pric5.set("")
        row5.set("")
        column5.set("")
        sec5.set("")
        cursor.close()
        conn.close()

def ShowView14():
    global viewform,Home
    Home=Tk()
    viewform = Toplevel()
    viewform.title("unit window")
    width = 900
    height = 600
    Home.config(bg='lawn green')
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm14()

def ViewForm14():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600,bg='lawn green')
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600,bg='lawn green')
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="DELI", font=('arial', 18),fg='black',bg='snow',relief=RAISED)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15),bg='lawn green')
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search14,fg='black',bg='snow',relief=RAISED)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset14,fg='black',bg='snow',relief=RAISED)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="back", command=DIS,fg='black',bg='snow',relief=RAISED)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="sections_map", command=t1,fg='black',bg='snow',relief=RAISED)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("PRODUCT_NAME","PRODUCT_PRICE","ROW_PLACED", "COLUMN_PLACED","SECTION"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('PRODUCT_NAME', text="PRODUCT_NAME",anchor=W)
    tree.heading('PRODUCT_PRICE', text="PRODUCT_PRICE",anchor=W)
    tree.heading('ROW_PLACED', text="ROW_PLACED",anchor=W)
    tree.heading('COLUMN_PLACED', text="COLUMN_PLACED",anchor=W)
    tree.heading('SECTION', text="SECTION",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)            
    tree.pack()
    DisplayData14()
    
def DisplayData14():
    Database()
    cursor.execute("SELECT * FROM `packed`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search14():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `packed` WHERE `prodn5` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset14():
    tree.delete(*tree.get_children())
    DisplayData14()
    SEARCH.set("")


###############################################################################################################################################################################################################

def ShowViewb():
    global viewform,Home
    Home=Tk()
    viewform = Toplevel()
    viewform.title("unit window")
    width = 900
    height = 600
    Home.config(bg='lawn green')
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewFormb()

def ViewFormb():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600,bg='lawn green')
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600,bg='lawn green')
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="DELI", font=('arial', 18),fg='black',bg='snow',relief=RAISED)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15),bg='lawn green')
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Searchb,fg='black',bg='snow',relief=RAISED)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Resetb,fg='black',bg='snow',relief=RAISED)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("PRODUCT_NAME","PRODUCT_PRICE","ROW_PLACED", "COLUMN_PLACED","SECTION"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('PRODUCT_NAME', text="PRODUCT_NAME",anchor=W)
    tree.heading('PRODUCT_PRICE', text="PRODUCT_PRICE",anchor=W)
    tree.heading('ROW_PLACED', text="ROW_PLACED",anchor=W)
    tree.heading('COLUMN_PLACED', text="COLUMN_PLACED",anchor=W)
    tree.heading('SECTION', text="SECTION",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)            
    tree.pack()
    DisplayDatab()
    
def DisplayDatab():
    Database()
    cursor.execute("SELECT * FROM `v1`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Searchb():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `v1` WHERE `prodn1` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Resetb():
    tree.delete(*tree.get_children())
    DisplayData14()
    SEARCH.set("")

###################################################################################
def open_window4():
    top1=Toplevel()
    top1.title("PACKED")
    top1.geometry('1700x700+0+0')
    top1.config(bg='lawn green')
    label2=Label(top1,text="PACKED GOODS",font=('arial',20,'bold'),fg='black',bg='snow',relief=RAISED)
    label2.pack(side=TOP,fill=X)
    
    MidForm1 = Frame(top1,width=700,height=700,bg='snow',relief=RAISED, bd=4)
    MidForm1.place(x=440,y=50)
    
    ru=Label(MidForm1,text="PRODUCT NAME",font=('arial',14,'bold'),fg='black',bg='snow')
    ru.place(x=0,y=10)
    ru1=Entry(MidForm1,textvariable=prod4name,font=('arial',14,'bold'))
    ru1.place(x=250,y=10)
    
    rn=Label(MidForm1,text="PRODUCT PRICE",font=('arial',14,'bold'),fg='black',bg='snow')
    rn.place(x=0,y=90)
    rename1= Entry(MidForm1, textvariable=pric5, font=('arial',14,'bold'))
    rename1.place(x=250,y=90)
    
    rmob=Label(MidForm1,text="ROW PLACED",font=('arial',14,'bold'),fg='black',bg='snow')
    rmob.place(x=0,y=170)
    rmob1=Entry(MidForm1,textvariable=row5,font=('arial',14,'bold'))
    rmob1.place(x=250,y=170)
    
    remail=Label(MidForm1,text="COLUMN PLACED",font=('arial',14,'bold'),fg='black',bg='snow')
    remail.place(x=0,y=250)
    remail1=Entry(MidForm1,textvariable=column5,font=('arial',14,'bold'))
    remail1.place(x=250,y=250)
    
    r1=Label(MidForm1,text="SECTION",font=('arial',14,'bold'),fg='black',bg='snow')
    r1.place(x=0,y=330)
    r11=Entry(MidForm1,textvariable=sec5,font=('arial',14,'bold'))
    r11.place(x=250,y=330)
    
    login10=Button(MidForm1,text= 'BACK TO HOMEPAGE',width=17,command=top1.destroy,bg='lawn green',fg='black',relief='raised')
    login10.place(x=250,y=490)

    but=Button(MidForm1,text='SUBMIT',relief="raised",bg='lawn green',fg='black',command=AddNew14)
    but.place(x=500,y=490)

    menubar = Menu(top1)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="View",command=ShowView14)
    menubar.add_cascade(label="VIEW_MENU", menu=filemenu)
    top1.config(menu=menubar)
    
#####################################################################################
    ##############################################################################################################
           
def open_window3():
    top1=Toplevel()
    top1.title("DRIED")
    top1.geometry('1700x700+0+0')
    top1.config(bg='lawn green')
    label2=Label(top1,text="DRY GOODS",font=('arial',20,'bold'),fg='black',bg='snow',relief=RAISED)
    label2.pack(side=TOP,fill=X)
    
    MidForm1 = Frame(top1,width=700,height=700,bg='snow',relief=RAISED, bd=4)
    MidForm1.place(x=440,y=50)
    
    ru=Label(MidForm1,text="PRODUCT NAME",font=('arial',14,'bold'),fg='black',bg='snow')
    ru.place(x=0,y=10)
    ru1=Entry(MidForm1,textvariable=prod3name,font=('arial',14,'bold'))
    ru1.place(x=250,y=10)
    
    rn=Label(MidForm1,text="PRODUCT PRICE",font=('arial',14,'bold'),fg='black',bg='snow')
    rn.place(x=0,y=90)
    rename1= Entry(MidForm1, textvariable=pric4, font=('arial',14,'bold'))
    rename1.place(x=250,y=90)
    
    rmob=Label(MidForm1,text="ROW PLACED",font=('arial',14,'bold'),fg='black',bg='snow')
    rmob.place(x=0,y=170)
    rmob1=Entry(MidForm1,textvariable=row4,font=('arial',14,'bold'))
    rmob1.place(x=250,y=170)
    
    remail=Label(MidForm1,text="COLUMN PLACED",font=('arial',14,'bold'),fg='black',bg='snow')
    remail.place(x=0,y=250)
    remail1=Entry(MidForm1,textvariable=column4,font=('arial',14,'bold'))
    remail1.place(x=250,y=250)
    
    r1=Label(MidForm1,text="SECTION",font=('arial',14,'bold'),fg='black',bg='snow')
    r1.place(x=0,y=330)
    r11=Entry(MidForm1,textvariable=sec4,font=('arial',14,'bold'))
    r11.place(x=250,y=330)
    
    login10=Button(MidForm1,text= 'BACK TO HOMEPAGE',width=17,command=top1.destroy,bg='lawn green',fg='black',relief='raised')
    login10.place(x=250,y=490)

    but=Button(MidForm1,text='SUBMIT',relief="raised",bg='lawn green',fg='black',command=AddNew13)
    but.place(x=500,y=490)

    menubar = Menu(top1)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="View",command=ShowView13)
    menubar.add_cascade(label="VIEW_MENU", menu=filemenu)
    top1.config(menu=menubar)
    
#####################################################################################
    ##############################################################################################################
           
def open_window2():
    top1=Toplevel()
    top1.title("HOME")
    top1.geometry('1700x700+0+0')
    top1.config(bg='lawn green')
    label2=Label(top1,text="HOME GOODS",font=('arial',20,'bold'),fg='black',bg='snow',relief=RAISED)
    label2.pack(side=TOP,fill=X)
    
    MidForm1 = Frame(top1,width=700,height=700,bg='snow',relief=RAISED, bd=4)
    MidForm1.place(x=440,y=50)
    
    ru=Label(MidForm1,text="PRODUCT NAME",font=('arial',14,'bold'),fg='black',bg='snow')
    ru.place(x=0,y=10)
    ru1=Entry(MidForm1,textvariable=prod2name,font=('arial',14,'bold'))
    ru1.place(x=250,y=10)
    
    rn=Label(MidForm1,text="PRODUCT PRICE",font=('arial',14,'bold'),fg='black',bg='snow')
    rn.place(x=0,y=90)
    rename1= Entry(MidForm1, textvariable=pric3, font=('arial',14,'bold'))
    rename1.place(x=250,y=90)
    
    rmob=Label(MidForm1,text="ROW PLACED",font=('arial',14,'bold'),fg='black',bg='snow')
    rmob.place(x=0,y=170)
    rmob1=Entry(MidForm1,textvariable=row3,font=('arial',14,'bold'))
    rmob1.place(x=250,y=170)
    
    remail=Label(MidForm1,text="COLUMN PLACED",font=('arial',14,'bold'),fg='black',bg='snow')
    remail.place(x=0,y=250)
    remail1=Entry(MidForm1,textvariable=column3,font=('arial',14,'bold'))
    remail1.place(x=250,y=250)
    
    r1=Label(MidForm1,text="SECTION",font=('arial',14,'bold'),fg='black',bg='snow')
    r1.place(x=0,y=330)
    r11=Entry(MidForm1,textvariable=sec3,font=('arial',14,'bold'))
    r11.place(x=250,y=330)
    
    login10=Button(MidForm1,text= 'BACK TO HOMEPAGE',width=17,command=top1.destroy,bg='lawn green',fg='black',relief='raised')
    login10.place(x=250,y=490)

    but=Button(MidForm1,text='SUBMIT',relief="raised",bg='lawn green',fg='black',command=AddNew12)
    but.place(x=500,y=490)

    menubar = Menu(top1)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="View",command=ShowView12)
    menubar.add_cascade(label="VIEW_MENU", menu=filemenu)
    top1.config(menu=menubar)
                                                                                                     
#####################################################################################
    ##############################################################################################################
           
def open_window1():                                   
    top1=Toplevel()
    top1.title("HEALTH AND BEAUTY")
    top1.geometry('1700x700+0+0')                                        
    top1.config(bg='lawn green')
    label2=Label(top1,text="HEALTH AND BEAUTY PRODUCTS",font=('arial',20,'bold'),fg='black',bg='snow',relief=RAISED)
    label2.pack(side=TOP,fill=X)
    
    MidForm1 = Frame(top1,width=700,height=700,bg='snow',relief=RAISED, bd=4)                                              
    MidForm1.place(x=440,y=50)
    
    ru=Label(MidForm1,text="PRODUCT NAME",font=('arial',14,'bold'),fg='black',bg='snow')
    ru.place(x=0,y=10)
    ru1=Entry(MidForm1,textvariable=prod1name,font=('arial',14,'bold'))
    ru1.place(x=250,y=10)
    
    rn=Label(MidForm1,text="PRODUCT PRICE",font=('arial',14,'bold'),fg='black',bg='snow')
    #rn=Label(MidForm1,text="PRODUCT PRICE",font=('arial',14,'bold'),fg='black',bg='snow')                                                              ')
    rn.place(x=0,y=90)
    rename1= Entry(MidForm1, textvariable=pric2, font=('arial',14,'bold'))
    rename1.place(x=250,y=90)
    
    rmob=Label(MidForm1,text="ROW PLACED",font=('arial',14,'bold'),fg='black',bg='snow')
    rmob.place(x=0,y=170)
    rmob1=Entry(MidForm1,textvariable=row2,font=('arial',14,'bold'))
    rmob1.place(x=250,y=170)
    
    remail=Label(MidForm1,text="COLUMN PLACED",font=('arial',14,'bold'),fg='black',bg='snow')
    remail.place(x=0,y=250)
    remail1=Entry(MidForm1,textvariable=column2,font=('arial',14,'bold'))
    remail1.place(x=250,y=250)
    
    r1=Label(MidForm1,text="SECTION",font=('arial',14,'bold'),fg='black',bg='snow')
    r1.place(x=0,y=330)
    r11=Entry(MidForm1,textvariable=sec2,font=('arial',14,'bold'))
    r11.place(x=250,y=330)
    
    login10=Button(MidForm1,text= 'BACK TO HOMEPAGE',width=17,command=top1.destroy,bg='lawn green',fg='black',relief='raised')
    login10.place(x=250,y=490)

    but=Button(MidForm1,text='SUBMIT',relief="raised",bg='lawn green',fg='black',command=AddNew11)
    but.place(x=500,y=490)

    menubar = Menu(top1)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="View",command=ShowView11)
    menubar.add_cascade(label="VIEW_MENU", menu=filemenu)
    top1.config(menu=menubar)
    
#####################################################################################
##############################################################################################################
           
def open_window():
    top1=Toplevel()
    top1.title("DELI")
    top1.geometry('1700x700+0+0')
    top1.config(bg='lawn green')
    label2=Label(top1,text="DELI PRODUCTS",font=('arial',20,'bold'),fg='black',bg='snow',relief=RAISED)
    label2.pack(side=TOP,fill=X)
    
    MidForm1 = Frame(top1,width=700,height=700,bg='snow',relief=RAISED, bd=4)
    MidForm1.place(x=440,y=50)
    
    ru=Label(MidForm1,text="PRODUCT NAME",font=('arial',14,'bold'),fg='black',bg='snow')
    ru.place(x=0,y=10)
    ru1=Entry(MidForm1,textvariable=prodname,font=('arial',14,'bold'))
    ru1.place(x=250,y=10)
    
    rn=Label(MidForm1,text="PRODUCT PRICE",font=('arial',14,'bold'),fg='black',bg='snow')
    rn.place(x=0,y=90)
    rename1= Entry(MidForm1, textvariable=pric1, font=('arial',14,'bold'))
    rename1.place(x=250,y=90)
    
    rmob=Label(MidForm1,text="ROW PLACED",font=('arial',14,'bold'),fg='black',bg='snow')
    rmob.place(x=0,y=170)
    rmob1=Entry(MidForm1,textvariable=row1,font=('arial',14,'bold'))
    rmob1.place(x=250,y=170)
    
    remail=Label(MidForm1,text="COLUMN PLACED",font=('arial',14,'bold'),fg='black',bg='snow')
    remail.place(x=0,y=250)
    remail1=Entry(MidForm1,textvariable=column1,font=('arial',14,'bold'))
    remail1.place(x=250,y=250)
    
    r1=Label(MidForm1,text="SECTION",font=('arial',14,'bold'),fg='black',bg='snow')
    r1.place(x=0,y=330)
    r11=Entry(MidForm1,textvariable=sec1,font=('arial',14,'bold'))
    r11.place(x=250,y=330)
    
    login10=Button(MidForm1,text= 'BACK TO HOMEPAGE',width=17,command=top1.destroy,bg='lawn green',fg='black',relief='raised')
    login10.place(x=250,y=490)

    but=Button(MidForm1,text='SUBMIT',relief="raised",bg='lawn green',fg='black',command=AddNew10)
    but.place(x=500,y=490)

    menubar = Menu(top1)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="View",command=ShowView10)
    menubar.add_cascade(label="VIEW_MENU", menu=filemenu)
    top1.config(menu=menubar)
########################################################################################  
def Home():
    home=Toplevel()
    home.title("MANAGER MODULE")
    home.geometry('1700x650+0+0')
    home.config(bg='lawn green')
    label7=Label(home,text="GROCERY SECTIONS",font=('arial',14,'bold'),fg='black',bg='snow',relief=RAISED)
    label7.pack(side=TOP,fill=X)

    login1=Button(home,text= 'DELI',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=open_window)
    login1.place(x=360,y=100)
    
    login2=Button(home,text= 'HEALTH&BEAUTY',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=open_window1)
    login2.place(x=860,y=100)
    
    login3=Button(home,text= 'HOME-GOODS',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=open_window2)
    login3.place(x=360,y=200)
    
    login4=Button(home,text= 'DRY-GOODS',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=open_window3)
    login4.place(x=860,y=200)
    
    login6=Button(home,text= 'PACKED-GOODS',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=open_window4)
    login6.place(x=610,y=300)
    
    login112=Button(home,text= 'HOMEPAGE',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=home.destroy)
    login112.place(x=610,y=500)
######################################################################################
def DIS():
    home=Toplevel()
    home.title("MANAGER MODULE")
    home.geometry('1700x650+0+0')
    home.config(bg='lawn green')
    label7=Label(home,text="GROCERY SECTIONS",font=('arial',14,'bold'),fg='black',bg='snow',relief=RAISED)
    label7.pack(side=TOP,fill=X)

    login1=Button(home,text= 'DELI',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=ShowView10)
    login1.place(x=360,y=100)
    
    login2=Button(home,text= 'HEALTH&BEAUTY',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=ShowView11)
    login2.place(x=860,y=100)
    
    login3=Button(home,text= 'HOME-GOODS',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=ShowView12)
    login3.place(x=360,y=200)
    
    login4=Button(home,text= 'DRY-GOODS',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=ShowView13)
    login4.place(x=860,y=200)
    
    login6=Button(home,text= 'PACKED-GOODS',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=ShowView14)
    login6.place(x=610,y=300)
    
    login112=Button(home,text= 'HOMEPAGE',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=home.destroy)
    login112.place(x=610,y=500)
        
#####################################################################################
def t1():
    import dope
    dope.t1()
''''

def t1():
    wn = turtle.Screen()     # creates a graphics window
    wn.setup(500,440)      # set window dimension

    t = turtle.Turtle()
    t.color('red')
    t.forward(100)
    t.left(90)
    t.forward(80)
    t.right(90)
    t.circle(36)
    t.write("DELI",move=False,align="center",font=('calibri',18,'bold'))
    b = turtle.Turtle()
    b.color('blue')
    b.left(90)
    b.forward(100)
    b.left(90)
    b.forward(50)
    b.circle(36)
    b.write("HEALTH",move=False,align="center",font=('calibri',18,'bold'))
    g = turtle.Turtle()
    g.color('green')
    g.right(90)
    g.forward(130)
    g.left(90)
    g.forward(50)
    g.circle(36)
    g.write("HOME",move=False,align="center",font=('calibri',18,'bold'))
    g1 = turtle.Turtle()
    g1.color('orange')
    g1.backward(110)
    g1.left(90)
    g1.forward(50)
    g1.circle(36)
    g1.write("DRIED",move=False,align="center",font=('calibri',18,'bold'))
    g2 = turtle.Turtle()
    g2.color('brown')
    g2.right(90)
    g2.forward(10)
    g2.right(90)
    g2.forward(110)
    g2.left(90)
    g2.forward(50)
    g2.circle(36)
    g2.write("PACKED",move=False,align="center",font=('calibri',18,'bold'))
'''
###################################################################################
def cust():
    home1=Toplevel()
    home1.title("MANAGER MODULE")
    home1.geometry('1700x350+0+0')
    home1.config(bg='lawn green')
    label7=Label(home1,text="CUSTOMER SECTIONS",font=('arial',14,'bold'),fg='black',bg='snow',relief=RAISED)
    label7.pack(side=TOP,fill=X)

    login1=Button(home1,text= 'SEARCH_BY_SECTION',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=DIS)
    login1.place(x=360,y=100)
    
    login2=Button(home1,text= 'SEARCH_BY_PRODUCT',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=ShowViewb)
    login2.place(x=860,y=100)
    
    
##################################################################################
#photo=PhotoImage(file=r"C:\\Users\\Baagyu Arun\\Desktop\\SQL\\pan.png")
#photolabel=Label(image=photo)
#photolabel.place(x=606,y=150)

#h=PhotoImage(file=r"C:\\Users\\Baagyu Arun\\Desktop\\SQL\\lam.png")
#back=Label(image=h)
#back.place(x=36,y=150)

login3=Button(root,text= 'CUSTOMER',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=cust)
login3.place(x=136,y=600)
    
login4=Button(root,text= 'MANAGER',font=('arial',14,'bold'),width=20,height=3,bg='snow',relief=RAISED,fg='black',command=Home)
login4.place(x=706,y=600)



root.mainloop()
