import sqlite3
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox


splash = tkinter.Tk()
splash.title("welcome to LIC")

splash_width = 789
splash_height = 269

screen_width= splash.winfo_screenwidth()
screen_height= splash.winfo_screenheight()

my_img = ImageTk.PhotoImage(Image.open("img.png"))
my_label = Label(image=my_img)
my_label.pack()
x = (screen_width/2)-(splash_width/2)
y = (screen_height/2)-(splash_height/2)

splash.overrideredirect(True)
splash.geometry(f'{splash_width}x{splash_height}+{int(x)}+{int(y)}')


def add_window():

    window1 = tkinter.Tk()
    window1.configure(bg="#0B023D")
    window1.title("Enter new Policy Holder")

    frame3 = LabelFrame(window1, text="LIC PRISMODATA", bg="#0B023D", fg="yellow")
    frame3.pack(padx=10, pady=10)

    frame007 = LabelFrame(frame3, padx=40, pady=40, bg="#1E0A4E", fg="white", bd=0)
    frame007.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    frame1 = LabelFrame(frame3, padx=40, pady=40, bg="#1E0A4E", fg="white", bd=0)
    frame1.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    f_name_label = Label(frame1, text="Full name", bg="#1E0A4E", fg="white")
    f_name_label.grid(row=0, column=0, sticky=W, padx=10 )
    f_name = Entry(frame1, width=30)
    f_name.grid(row=0, column=1, padx=10, pady=5)

    phone_label = Label(frame1, text="Phone number", bg="#1E0A4E", fg="white")
    phone_label.grid(row=1, column=0, sticky=W, padx=10 )
    phone = Entry(frame1, width=30)
    phone.grid(row=1, column=1, pady=5)

    number_label = Label(frame1, text="Policy Number", bg="#1E0A4E", fg="white")
    number_label.grid(row=2, column=0, sticky=W, padx=10)
    number = Entry(frame1, width=30)
    number.grid(row=2, column=1, pady=5)

    dob_label = Label(frame1, text="DOB", bg="#1E0A4E", fg="white")
    dob_label.grid(row=3, column=0, sticky=W, padx=10)
    date_entry1 = DateEntry(frame1, font=('Helvetica', 8, 'bold'), date_pattern='dd/mm/yy')
    date_entry1.grid(row=3, column=1, pady=5, padx=10, sticky=W + E)

    nominee_label = Label(frame1, text="Nominee Name", bg="#1E0A4E", fg="white")
    nominee_label.grid(row=4, column=0, sticky=W, padx=10)
    nominee = Entry(frame1, width=30)
    nominee.grid(row=4, column=1, pady=5)

    nominee_relation_label = Label(frame1, text="Nominee Relation", bg="#1E0A4E", fg="white")
    nominee_relation_label.grid(row=5, column=0, sticky=W, padx=10)
    nominee_relation = Entry(frame1, width=30)
    nominee_relation.grid(row=5, column=1, pady=5)

    amount_label = Label(frame1, text="Premium Amount", bg="#1E0A4E", fg="white")
    amount_label.grid(row=6, column=0, sticky=W, padx=10)
    amount = Entry(frame1, width=30)
    amount.grid(row=6, column=1, pady=5)

    current_label = Label(frame1, text="Current due date", bg="#1E0A4E", fg="white")
    current_label.grid(row=7, column=0, sticky=W, padx=10 )
    date_entry = DateEntry(frame1,font=('Helvetica', 8, 'bold'), date_pattern='dd/mm/yy')
    date_entry.grid(row=7, column=1, pady=5, padx=10, sticky=W + E)

    mode_label = Label(frame1, text="Mode", bg="#1E0A4E", fg="white")
    mode_label.grid(row=8, column=0, sticky=W, padx=10)
    menu1 = ttk.Combobox(frame1, text="SELECT", value=["Yearly", "Half Yearly", "Quarterly"])
    menu1.current(0)
    menu1.grid(row=8, column=1, pady=5, padx=10, sticky=W+E)

    term_label = Label(frame1, text="Term", bg="#1E0A4E", fg="white")
    term_label.grid(row=9, column=0, sticky=W, padx=10)
    term = Entry(frame1, width=30)
    term.grid(row=9, column=1, pady=5)

    m_amount_label = Label(frame1, text="Maturity Amount", bg="#1E0A4E", fg="white")
    m_amount_label.grid(row=10, column=0, sticky=W, padx=10)
    m_amount = Entry(frame1, width=30)
    m_amount.grid(row=10, column=1, pady=5)

    m_date_label = Label(frame1, text="Maturity Date", bg="#1E0A4E", fg="white")
    m_date_label.grid(row=11, column=0, sticky=W, padx=10)
    date_entry3 = DateEntry(frame1, font=('Helvetica', 8, 'bold'), date_pattern='dd/mm/yy')
    date_entry3.grid(row=11, column=1, pady=5, padx=10, sticky=W + E)

    address_label = Label(frame1, text="Address", bg="#1E0A4E", fg="white")
    address_label.grid(row=12, column=0, sticky=W, padx=10)
    address = Entry(frame1, width=30)
    address.grid(row=12, column=1, pady=5, ipady=10)

    b = Button(frame1, text="CLOSE", command=window1.destroy, fg='white', bg='red',font=('Helvetica', 10, 'bold'), bd=0)
    b.grid(row=13, column=0, sticky=W+E)

    def submit():
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        c.execute("INSERT INTO customer VALUES (:a, :b, :c, :d, :e, :f, :g, :h, :i, :j, :k, :l, :m)", {'a': f_name.get(), 'b': phone.get(), 'c': number.get(), 'd': date_entry.get(), 'e': nominee.get(), 'f': nominee_relation.get(), 'g': amount.get(), 'h': date_entry1.get(), 'i': menu1.get(), 'j': term.get(), 'k': m_amount.get(), 'l': date_entry3.get(), 'm': address.get()})

        conn.commit()
        conn.close()

        f_name.delete(0, END)
        phone.delete(0, END)
        number.delete(0, END)
        nominee.delete(0, END)
        nominee_relation.delete(0, END)
        amount.delete(0, END)
        term.delete(0, END)
        m_amount.delete(0, END)
        address.delete(0, END)

        messagebox.showinfo('PRISMODATA', 'Data added successfully')

    b1 = Button(frame1, command=submit, text="SUBMIT POLICY", fg='white', bg='#1F77F9', font=('Helvetica', 10, 'bold'), bd=0)
    b1.grid(row=13, column=1, padx=10, pady=10, sticky=W + E)


def premium():
    kd = tkinter.Tk()
    kd.title("Premium Due")
    kd.configure(background='#0B023D')

    wind3 = LabelFrame(kd, background='#1E0A4E', text="SEARCH PREMIUM DUES", fg="yellow")
    wind3.grid(row=0, padx=10, pady=10)
    windoo3 = LabelFrame(kd, background='#1E0A4E', text="OUTPUT RESULT", fg="yellow")
    windoo3.grid(row=1, padx=10, pady=10)
    hgh = LabelFrame(windoo3, background='#1E0A4E', bd=0)
    hgh.grid()

    tree_scroll = Scrollbar(hgh)
    tree_scroll.pack(side=RIGHT, fill=Y)
    trv = ttk.Treeview(hgh, column=(1, 2, 3, 4), show="headings", yscrollcommand=tree_scroll.set)
    trv.pack(padx= 10, pady= 10)

    tree_scroll.config(command=trv.yview)
    trv.column(1, anchor=W)
    trv.column(2, anchor=W)
    trv.column(3, anchor=W)
    trv.column(4, anchor=W)

    trv.heading(1, text="Full Name", anchor=W)
    trv.heading(2, text="Phone", anchor=W)
    trv.heading(3, text="Policy No.", anchor=W)
    trv.heading(4, text="DOB", anchor=W)

    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('', 'end', values=i)

    def kong():
        conn1 = sqlite3.connect('user_data.db')
        c1 = conn1.cursor()
        q2 = search_box.get()
        sql2 = "SELECT fname, phone, pnumber, dob from customer WHERE due LIKE '%" + q2 + "%'"
        c1.execute(sql2)
        rows = c1.fetchall()
        update(rows)

    q = StringVar()
    query = "SELECT fname, phone, pnumber, dob from customer"
    c.execute(query)
    rows = c.fetchall()

    update(rows)

    def export():
        return 0

    search_box = DateEntry(wind3, width=30, font=('Helvetica', 8, 'bold'), date_pattern='dd/mm/yy')
    search_box.grid(row=0, column=0, padx=10, pady=10)
    search_box_button = Button(wind3, text="SEARCH", command=kong, fg='white', bg='#1F77F9',
                               font=('Helvetica', 10, 'bold'), width=20, bd=0)
    search_box_button.grid(row=0, column=1, padx=30)
    export = Button(wind3, text="EXPORT", command=export, fg='white', bg='#1F77F9', font=('Helvetica', 10, 'bold'), width=20, bd=0)
    export.grid(row=0, column=2)
    out = Button(wind3, text="EXIT", command=kd.destroy, fg='white', bg='red', font=('Helvetica', 10, 'bold'), width=20, bd=0)
    out.grid(row=0, column=3, padx=30)

    conn.commit()
    conn.close()


def new_plan():
    window2 = tkinter.Tk()
    window2.configure(background='#0B023D')
    window2.title('Add New Plan')
    fram1 = LabelFrame(window2, text="ADD NEW LIC POLICY PLAN", bg="#1E0A4E", fg="yellow",font=('Helvetica', 10, 'bold'))
    fram1.grid(padx=10, pady=10)
    fram2 = LabelFrame(fram1, bg="#1E0A4E", fg="yellow",
                       font=('Helvetica', 10, 'bold'), bd=0)
    fram2.grid(padx=20, pady=20)

    plan_label = Label(fram2, text="Plan name", bg="#1E0A4E", fg="white")
    plan_label.grid(row=0, column=0, sticky=W, padx=10)
    plan = Entry(fram2, width=30)
    plan.grid(row=0, column=1, pady=5)

    age_label = Label(fram2, text="Age limit", bg="#1E0A4E", fg="white")
    age_label.grid(row=1, column=0, sticky=W, padx=10)
    age = Entry(fram2, width=30)
    age.grid(row=1, column=1, pady=5)

    tinv_label = Label(fram2, text="total investment", bg="#1E0A4E", fg="white")
    tinv_label.grid(row=2, column=0, sticky=W, padx=10)
    tinv = Entry(fram2, width=30)
    tinv.grid(row=2, column=1, pady=5)

    q_label = Label(fram2, text="Quarterly premium amount", bg="#1E0A4E", fg="white")
    q_label.grid(row=3, column=0, sticky=W, padx=10)
    q = Entry(fram2, width=30)
    q.grid(row=3, column=1, pady=5)

    y1_label = Label(fram2, text="Yearly premium amount", bg="#1E0A4E", fg="white")
    y1_label.grid(row=4, column=0, sticky=W, padx=10)
    y1 = Entry(fram2, width=30)
    y1.grid(row=4, column=1, pady=5)

    hy_label = Label(fram2, text="Half yearly premium amount", bg="#1E0A4E", fg="white")
    hy_label.grid(row=5, column=0, sticky=W, padx=10)
    hy = Entry(fram2, width=30)
    hy.grid(row=5, column=1, pady=5)

    minsum_label = Label(fram2, text="Minimum sum assured", bg="#1E0A4E", fg="white")
    minsum_label.grid(row=6, column=0, sticky=W, padx=10)
    minsum = Entry(fram2, width=30)
    minsum.grid(row=6, column=1, pady=5)

    maxsum_label = Label(fram2, text="Maximum sum assured", bg="#1E0A4E", fg="white")
    maxsum_label.grid(row=7, column=0, sticky=W, padx=10)
    maxsum = Entry(fram2, width=30)
    maxsum.grid(row=7, column=1, pady=5)

    desc_label = Label(fram2, text="Policy description", bg="#1E0A4E", fg="white")
    desc_label.grid(row=8, column=0, sticky=W, padx=10)
    desc = Entry(fram2, width=30)
    desc.grid(row=8, column=1, pady=5)

    b1 = Button(fram2, text="CLOSE", command=window2.destroy, fg='white', bg='red',font=('Helvetica', 10, 'bold'), bd=0)
    b1.grid(row=9, column=0, sticky=W+E, padx=10)

    def submit1():
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        c.execute("INSERT INTO policy VALUES (:a, :b, :c, :d, :e, :f, :g, :h, :i)", {'a': plan.get(), 'b': age.get(), 'c': tinv.get(), 'd': q.get(), 'e': y1.get(), 'f': hy.get(), 'g': minsum.get(), 'h': maxsum.get(), 'i': desc.get()})

        conn.commit()
        conn.close()

        plan.delete(0, END)
        age.delete(0, END)
        tinv.delete(0, END)
        q.delete(0, END)
        y1.delete(0, END)
        hy.delete(0, END)
        minsum.delete(0, END)
        maxsum.delete(0, END)
        desc.delete(0, END)

        messagebox.showinfo('PRISMODATA', 'Policy added successfully')

    b3 = Button(fram2, command=submit1, text="SUBMIT POLICY", fg='white', bg='#1F77F9', font=('Helvetica', 10, 'bold'), bd=0)
    b3.grid(row=9, column=1, pady=10, sticky=W + E)



def maturity():
    kd = tkinter.Tk()
    kd.configure(background='#0B023D')
    kd.title("Maturity Due")

    wind3 = LabelFrame(kd, background='#1E0A4E', text="SEARCH MATURITY DUES", fg="yellow")
    wind3.grid(row=0, padx=10, pady=10)
    windoo3 = LabelFrame(kd, background='#1E0A4E', text="OUTPUT RESULT", fg="yellow")
    windoo3.grid(row=1, padx=10, pady=10)
    hgh = LabelFrame(windoo3, background='#1E0A4E', bd=0)
    hgh.grid()
    tree_scroll = Scrollbar(hgh)
    tree_scroll.pack(side=RIGHT, fill=Y)
    trv = ttk.Treeview(hgh, column=(1, 2, 3, 4), show="headings", yscrollcommand=tree_scroll.set)
    trv.pack(padx=10, pady=10)

    tree_scroll.config(command=trv.yview)
    trv.column(1, anchor=W)
    trv.column(2, anchor=W)
    trv.column(3, anchor=W)
    trv.column(4, anchor=W)

    trv.heading(1, text="Full Name", anchor=W)
    trv.heading(2, text="Phone", anchor=W)
    trv.heading(3, text="Policy No.", anchor=W)
    trv.heading(4, text="Maturity Amount", anchor=W)

    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('', 'end', values=i)

    def kong():
        conn1 = sqlite3.connect('user_data.db')
        c1 = conn1.cursor()
        q2 = search_box.get()
        sql2 = "SELECT fname, phone, pnumber, mamount from customer WHERE mdate LIKE '%" + q2 + "%'"
        c1.execute(sql2)
        rows = c1.fetchall()
        update(rows)

    q = StringVar()
    query = "SELECT fname, phone, pnumber, mamount from customer"
    c.execute(query)
    rows = c.fetchall()

    update(rows)

    def export():
        return 0

    search_box = DateEntry(wind3, width=30, font=('Helvetica', 8, 'bold'), date_pattern='dd/mm/yy')
    search_box.grid(row=0, column=0, padx=10, pady=10)
    search_box_button = Button(wind3, text="SEARCH", command=kong, fg='white', bg='#1F77F9',
                               font=('Helvetica', 10, 'bold'), width=20, bd=0)
    search_box_button.grid(row=0, column=1, padx=30)
    export = Button(wind3, text="EXPORT", command=export, fg='white', bg='#1F77F9', font=('Helvetica', 10, 'bold'),
                    width=20, bd=0)
    export.grid(row=0, column=2)
    out = Button(wind3, text="EXIT", command=kd.destroy, fg='white', bg='red', font=('Helvetica', 10, 'bold'), width=20,
                 bd=0)
    out.grid(row=0, column=3, padx=30)

    conn.commit()
    conn.close()


def mod():
    window1 = tkinter.Tk()
    window1.configure(bg="#0B023D")
    window1.title("Edit Data")

    frame3 = LabelFrame(window1, text="LIC PRISMODATA", bg="#0B023D", fg="yellow")
    frame3.pack(padx=10, pady=10)

    frame007 = LabelFrame(frame3, padx=40, pady=40, bg="#0B023D", fg="white", bd=0)
    frame007.grid(row=0, column=0, padx=0, pady=10, sticky=W)

    def edit():
        conn1 = sqlite3.connect('user_data.db')
        c1 = conn1.cursor()
        q1 = bond.get()
        c1.execute("SELECT * from customer WHERE pnumber LIKE '%" + q1 + "%'")
        records = c.fetchall()

        for record in records:
            newton.insert(0, record[0])
            newton1.insert(0, record[1])
            newton2.insert(0, record[2])
            newton3.insert(0, record[3])
            newton4.insert(0, record[4])
            newton5.insert(0, record[5])
            newton6.insert(0, record[6])
            newton7.insert(0, record[7])
            newton8.insert(0, record[8])
            newton9.insert(0, record[9])
            newton10.insert(0, record[10])
            newton11.insert(0, record[11])
            newton12.insert(0, record[12])
        conn1.commit()
        conn1.close()

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('', 'end', values=i)

    def kong():
        conn1 = sqlite3.connect('user_data.db')
        c1 = conn1.cursor()
        q2 = bond.get()
        sql2 = "SELECT fname, pnumber, dob, amount, mamount from customer WHERE pnumber LIKE '%" + q2 + "%'"
        c1.execute(sql2)
        rows = c1.fetchall()
        update(rows)

    frame0071 = LabelFrame(frame007, padx=40, pady=40, bg="#1E0A4E", fg="white", bd=0)
    frame0071.grid(row=0, column=0, padx=0, pady=10)

    james_bond = Label(frame0071, text="Policy Number", bg="#1E0A4E", fg="white")
    james_bond.grid(row=0, column=0, sticky=W, padx=10)
    bond = Entry(frame0071, width=30)
    bond.grid(row=0, column=1, padx=10, pady=5)

    frame0072 = LabelFrame(frame007, padx=40, pady=40, bg="#1E0A4E", fg="white", bd=0)
    frame0072.grid(row=1, column=0)
    tree_scroll = Scrollbar(frame0072)
    tree_scroll.pack(side=RIGHT, fill=Y)
    trv = ttk.Treeview(frame0072, column=(1, 2, 3, 4, 5), show="headings", yscrollcommand=tree_scroll.set)
    trv.pack()

    tree_scroll.config(command=trv.yview)
    trv.column(1, anchor=W, width="80")
    trv.column(2, anchor=W, width="80")
    trv.column(3, anchor=W, width="40")
    trv.column(4, anchor=W, width="40")
    trv.column(5, anchor=W, width="40")

    trv.heading(1, text="Full Name", anchor=W)
    trv.heading(4, text="Premium Amount", anchor=W)
    trv.heading(2, text="Policy No.", anchor=W)
    trv.heading(3, text="DOB", anchor=W)
    trv.heading(5, text="Maturity Amount", anchor=W)

    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()

    query = "SELECT fname, pnumber, dob, amount, mamount from customer"
    c.execute(query)
    rows = c.fetchall()
    update(rows)

    frame1 = LabelFrame(frame3, padx=40, pady=40, bg="#1E0A4E", fg="white", bd=0)
    frame1.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    f_name_label = Label(frame1, text="Full name", bg="#1E0A4E", fg="white")
    f_name_label.grid(row=0, column=0, sticky=W, padx=10)
    newton = Entry(frame1, width=30)
    newton.grid(row=0, column=1, padx=10, pady=5)

    phone_label = Label(frame1, text="Phone number", bg="#1E0A4E", fg="white")
    phone_label.grid(row=1, column=0, sticky=W, padx=10)
    newton1 = Entry(frame1, width=30)
    newton1.grid(row=1, column=1, pady=5)

    number_label = Label(frame1, text="Policy Number", bg="#1E0A4E", fg="white")
    number_label.grid(row=2, column=0, sticky=W, padx=10)
    newton2 = Entry(frame1, width=30)
    newton2.grid(row=2, column=1, pady=5)

    dob_label = Label(frame1, text="DOB", bg="#1E0A4E", fg="white")
    dob_label.grid(row=3, column=0, sticky=W, padx=10)
    newton3 = DateEntry(frame1, font=('Helvetica', 8, 'bold'), date_pattern='dd/mm/yy')
    newton3.grid(row=3, column=1, pady=5, padx=10, sticky=W + E)

    nominee_label = Label(frame1, text="Nominee Name", bg="#1E0A4E", fg="white")
    nominee_label.grid(row=4, column=0, sticky=W, padx=10)
    newton4 = Entry(frame1, width=30)
    newton4.grid(row=4, column=1, pady=5)

    nominee_relation_label = Label(frame1, text="Nominee Relation", bg="#1E0A4E", fg="white")
    nominee_relation_label.grid(row=5, column=0, sticky=W, padx=10)
    newton5 = Entry(frame1, width=30)
    newton5.grid(row=5, column=1, pady=5)

    amount_label = Label(frame1, text="Premium Amount", bg="#1E0A4E", fg="white")
    amount_label.grid(row=6, column=0, sticky=W, padx=10)
    newton6 = Entry(frame1, width=30)
    newton6.grid(row=6, column=1, pady=5)

    current_label = Label(frame1, text="Current due date", bg="#1E0A4E", fg="white")
    current_label.grid(row=7, column=0, sticky=W, padx=10)
    newton7 = DateEntry(frame1, font=('Helvetica', 8, 'bold'), date_pattern='dd/mm/yy')
    newton7.grid(row=7, column=1, pady=5, padx=10, sticky=W + E)

    mode_label = Label(frame1, text="Mode", bg="#1E0A4E", fg="white")
    mode_label.grid(row=8, column=0, sticky=W, padx=10)
    newton8 = ttk.Combobox(frame1, text="SELECT", value=["Yearly", "Half Yearly", "Quarterly"])
    newton8.current(0)
    newton8.grid(row=8, column=1, pady=5, padx=10, sticky=W + E)

    term_label = Label(frame1, text="Term", bg="#1E0A4E", fg="white")
    term_label.grid(row=9, column=0, sticky=W, padx=10)
    newton9 = Entry(frame1, width=30)
    newton9.grid(row=9, column=1, pady=5)

    m_amount_label = Label(frame1, text="Maturity Amount", bg="#1E0A4E", fg="white")
    m_amount_label.grid(row=10, column=0, sticky=W, padx=10)
    newton10 = Entry(frame1, width=30)
    newton10.grid(row=10, column=1, pady=5)

    m_date_label = Label(frame1, text="Maturity Date", bg="#1E0A4E", fg="white")
    m_date_label.grid(row=11, column=0, sticky=W, padx=10)
    newton11 = DateEntry(frame1, font=('Helvetica', 8, 'bold'), date_pattern='dd/mm/yy')
    newton11.grid(row=11, column=1, pady=5, padx=10, sticky=W + E)

    address_label = Label(frame1, text="Address", bg="#1E0A4E", fg="white")
    address_label.grid(row=12, column=0, sticky=W, padx=10)
    newton12 = Entry(frame1, width=30)
    newton12.grid(row=12, column=1, pady=5, ipady=10)

    boond = Button(frame0071, text="CLOSE", command=window1.destroy, fg='white', bg='red', font=('Helvetica', 10, 'bold'),bd=0)
    boond.grid(row=1, column=0, sticky=W + E)
    bond1 = Button(frame0071, command=edit, text="EDIT", fg='white', bg='#1F77F9', font=('Helvetica', 10, 'bold'),bd=0)
    bond1.grid(row=1, column=1, padx=10, pady=10, sticky=W + E)
    bond2 = Button(frame0071, command=kong, text="SEARCH", fg='white', bg='#1F77F9', font=('Helvetica', 10, 'bold'),bd=0)
    bond2.grid(row=2, column=1, padx=10, pady=0, sticky=W + E)

    def user_update():
        conn11 = sqlite3.connect('user_data.db')
        c11 = conn11.cursor()
        q1 = bond.get()
        c11.execute('''
        "UPDATE customer SET 
        fname = :a, 
        phone =:b, 
        dob=:d, 
        nname=:e, 
        nrelation=:f, 
        amount=:g, 
        due=:h, 
        mode=:i, 
        term=:j, 
        mamount=:k, 
        mdate=:l, 
        address=:m WHERE pnumber=:n", 
        {'a': newton.get(),
        'b': newton1.get(),
        'd': newton3.get(),
        'e': newton4.get(),
        'f': newton5.get(),
        'g': newton6.get(),
        'h': newton7.get(),
        'i': newton8.get(),
        'j': newton9.get(),
        'k': newton10.get(),
        'l': newton11.get(), 
        'n':q1}''')

        conn11.commit()
        conn11.close()

    b1 = Button(frame1, command=user_update, text="UPDATE POLICY", fg='white', bg='#1F77F9', font=('Helvetica', 10, 'bold'), bd=0)
    b1.grid(row=13, column=1, padx=10, pady=10, sticky=W + E)


def policies():

    kd = tkinter.Tk()
    kd.configure(background='#0B023D')
    kd.title("Plan INFO")

    wind3 = LabelFrame(kd, background='#1E0A4E', text="SEARCH PLANS", fg="yellow")
    wind3.grid(row=0, padx=10, pady=10)
    windoo3 = LabelFrame(kd, background='#1E0A4E', text="OUTPUT RESULT", fg="yellow")
    windoo3.grid(row=1, padx=10, pady=10)
    hgh = LabelFrame(windoo3, background='#1E0A4E', bd=0)
    hgh.grid()

    trv = ttk.Treeview(hgh, column=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings")
    trv.pack(padx=10, pady=10)

    trv.column(1, anchor=W, width="120")
    trv.column(2, anchor=W, width="80")
    trv.column(3, anchor=W, width="80")
    trv.column(4, anchor=W, width="80")
    trv.column(5, anchor=W, width="80")
    trv.column(6, anchor=W, width="80")
    trv.column(7, anchor=W, width="80")
    trv.column(8, anchor=W, width="80")
    trv.column(9, anchor=W, width="120")

    trv.heading(1, text="Policy name", anchor=W)
    trv.heading(2, text="Age", anchor=W)
    trv.heading(3, text="Investment", anchor=W)
    trv.heading(4, text="Q Premium", anchor=W)
    trv.heading(5, text="Y Premium", anchor=W)
    trv.heading(6, text="HY Premium", anchor=W)
    trv.heading(7, text="Minimum Sum Assured", anchor=W)
    trv.heading(8, text="Maximum Sym Assured", anchor=W)
    trv.heading(9, text="Description", anchor=W)

    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('', 'end', values=i)

    def kong():
        conn1 = sqlite3.connect('user_data.db')
        c1 = conn1.cursor()
        q2 = search_box.get()
        sql2 = "SELECT plan, age, tinv, q, y1, hy, minsum, maxsum, desc from policy WHERE plan LIKE '%" + q2 + "%'"
        c1.execute(sql2)
        rows = c1.fetchall()
        update(rows)

    q = StringVar()
    query = "SELECT plan, age, tinv, q, y1, hy, minsum, maxsum, desc from policy"
    c.execute(query)
    rows = c.fetchall()

    update(rows)

    def export():
        return 0

    search_box = Entry(wind3, width=30, font=('Helvetica', 8, 'bold'))
    search_box.grid(row=0, column=0, padx=10, pady=10)
    search_box_button = Button(wind3, text="SEARCH", command=kong, fg='white', bg='#1F77F9',
                               font=('Helvetica', 10, 'bold'), width=20, bd=0)
    search_box_button.grid(row=0, column=1, padx=30)
    export = Button(wind3, text="EXPORT", command=export, fg='white', bg='#1F77F9', font=('Helvetica', 10, 'bold'),
                    width=20, bd=0)
    export.grid(row=0, column=2)
    out = Button(wind3, text="EXIT", command=kd.destroy, fg='white', bg='red', font=('Helvetica', 10, 'bold'), width=20,
                 bd=0)
    out.grid(row=0, column=3, padx=30)

    conn.commit()
    conn.close()


def main_window():
    splash.destroy()
    wind = tkinter.Tk()
    wind.configure(background='#0B023D')
    wind.title("PRISMODATA")

    windo = LabelFrame(wind,text="PREMIUM VERSION", background='#0B023D',fg="YELLOW")
    windo.grid(row=1, padx=10, pady=10)
    windoww = LabelFrame(windo, background='#0B023D',bd=0)
    windoww.grid(row=0, column=0)
    f1 = Label(windoww, text="WELCOME TO PRISMODATA", font=('Helvetica', 20, 'bold'), fg="#1F77F9", bg='#0B023D')
    f1.grid(row=0, pady=20, sticky=E + W)
    window = LabelFrame(windoww, background='#0B023D')
    window.grid(row=1, column=0, padx=30, pady=10)

    frame = LabelFrame(window, padx=20, pady=20, bg="#1E0A4E", fg="pink",bd=0)
    frame.grid(row=0, column=0, padx=5, pady=5)
    sk = Label(frame, text="NEW POLICY HOLDER", font=('Helvetica', 11, 'bold'), bg="#1E0A4E", fg="white", borderwidth=1, relief='groove')
    sk.grid(row=0, sticky=W+E)
    sk = Label(frame, text="ADD NEW POLICY HOLDER", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=1, sticky=W, pady=5)
    sk = Label(frame, text="Click OPEN to continue", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=2, sticky=W)
    b = Button(frame, text="OPEN", command=add_window, width=40, fg='white', bg='#1F77F9',font=('Helvetica',10,'bold'), bd=0)
    b.grid(row=3,  pady=5)

    far = LabelFrame(window, padx=20, pady=20, bg="#1E0A4E", fg="#1E0A4E", bd=0)
    far.grid(row=1, column=0, padx=5, pady=5)
    sk = Label(far, text="MODIFY EXISTING DATA", font=('Helvetica', 11, 'bold'), bg="#1E0A4E", fg="white", borderwidth=1, relief='groove')
    sk.grid(row=0, sticky=W + E)
    sk = Label(far, text="MODIFY EXISTING POLICY HOLDER", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=1, sticky=W, pady=5)
    sk = Label(far, text="Click OPEN to continue", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=2, sticky=W)
    c = Button(far, text="OPEN", command=mod, width=40, fg='white', bg='#1F77F9',font=('Helvetica',10,'bold'), bd=0)
    c.grid( row=3, pady=5)

    far1 = LabelFrame(window, padx=20, pady=20, bg="#1E0A4E", fg="#1E0A4E", bd=0)
    far1.grid(row=2, column=0, padx=5, pady=5)
    sk = Label(far1, text="NEW PLAN ENTRY", font=('Helvetica', 11, 'bold'), bg="#1E0A4E", fg="white", borderwidth=1, relief='groove')
    sk.grid(row=0, sticky=W + E)
    sk = Label(far1, text="ADD NEW LIC PLANS", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=1, sticky=W, pady=5)
    sk = Label(far1, text="Click OPEN to continue", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=2, sticky=W)
    d = Button(far1, text="OPEN", command=new_plan, width=40, fg='white', bg='#1F77F9',font=('Helvetica',10,'bold'), bd=0)
    d.grid(row=3, pady=5)

    far2 = LabelFrame(window, padx=20, pady=20, bg="#1E0A4E", fg="pink", bd=0)
    far2.grid(row=0, column=1, padx=5, pady=5)
    sk = Label(far2, text="PLAN INFO", font=('Helvetica', 11, 'bold'), bg="#1E0A4E", fg="white", borderwidth=1, relief='groove')
    sk.grid(row=0, sticky=W + E)
    sk = Label(far2, text="ALL PLANS OF LIC", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=1, sticky=W, pady=5)
    sk = Label(far2, text="Click OPEN to continue", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=2, sticky=W)
    e = Button(far2, text="OPEN", command=policies, width=40, fg='white', bg='#1F77F9', font=('Helvetica',10,'bold'), bd=0)
    e.grid(row=3, pady=5)

    far3 = LabelFrame(window, padx=20, pady=20, bg="#1E0A4E", fg="#1E0A4E", bd=0)
    far3.grid(row=1, column=1, padx=5, pady=5)
    sk = Label(far3, text="PREMIUM DUES", font=('Helvetica', 11, 'bold'), bg="#1E0A4E", fg="white", borderwidth=1, relief='groove')
    sk.grid(row=0, sticky=W + E)
    sk = Label(far3, text="LIST OF PENDING PREMIUMS", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=1, sticky=W, pady=5)
    sk = Label(far3, text="Click OPEN to continue", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=2, sticky=W)
    f = Button(far3, text="OPEN", command=premium, width=40, fg='white', bg='#1F77F9',font=('Helvetica',10,'bold'), bd=0)
    f.grid(row=3, pady=5)

    far4 = LabelFrame(window, padx=20, pady=20, bg="#1E0A4E", fg="#1E0A4E" , bd=0)
    far4.grid(row=2, column=1, padx=5, pady=5)
    sk = Label(far4, text="MATURITY DUES", font=('Helvetica', 11, 'bold'), bg="#1E0A4E", fg="white", borderwidth=1, relief='groove')
    sk.grid(row=0, sticky=W + E)
    sk = Label(far4, text="LIST OF MATURED POLICIES", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=1, sticky=W, pady=5)
    sk = Label(far4, text="Click OPEN to continue", font=('Helvetica', 10), bg="#1E0A4E", fg="white")
    sk.grid(row=2, sticky=W)
    g = Button(far4, text="OPEN", command=maturity, width=40, fg='white', bg='#1F77F9',font=('Helvetica',10,'bold') , bd=0)
    g.grid(row=3, pady=5)

    detail11 = LabelFrame(windo, font=('Helvetica', 12, 'bold'), bg="#1E0A4E",fg="white", bd=0)
    detail11.grid(row=0, column=1, padx=10, pady=10)
    detail1 = LabelFrame(detail11, text="LIC PRISMODATA", padx=20, pady=20, font=('Helvetica', 12, 'bold'), bg="#1E0A4E",fg="white", )
    detail1.grid(row=0,column=0,padx=10)

    k = "LIC PRISMODATA is a GUI based Data base management software ,"
    k2 = "where the data of the policy holders could be stored and the "
    k3 = "queries could be run to  search the particular record ."
    k4 = "The purpose of this software is to help LIC agent’s to manage "
    k5 = "their client record in efficient and effective manner decreasing "
    k6 = "the paper work. The main objective of this software is to give provide"
    k7 = "a platform where the major tasks like client’s data basic information, "
    k8 = "premium due, due date, maturity date that will not make it hassle free "
    k9 = "for the agents to deal with these things but will also save lot of time. "
    k10 = "The system carrier out few automatic calculations for next premium due "
    k11 = "date, loan calculation, maturity date. This software will also facilitate "
    k12 = "the agent in selling new policies by providing the major details of the "
    k13 = "customer which is needed to filled during sell of new policy to the existing"
    k14 = " costumer of same agency. "

    f_name_label1 = Label(detail1, text=k, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label1.grid(row=0, column=0)
    f_name_label2 = Label(detail1, text=k2, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label2.grid(row=1, column=0)
    f_name_label3 = Label(detail1, text=k3, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label3.grid(row=2, column=0)
    f_name_label4 = Label(detail1, text=k4, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label4.grid(row=4, column=0)
    f_name_label5 = Label(detail1, text=k5, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label5.grid(row=5, column=0)
    f_name_label6 = Label(detail1, text=k6, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label6.grid(row=6, column=0)
    f_name_label7 = Label(detail1, text=k7, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label7.grid(row=7, column=0)
    f_name_label8 = Label(detail1, text=k8, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label8.grid(row=8, column=0)
    f_name_label9 = Label(detail1, text=k9, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label9.grid(row=9, column=0)
    f_name_label10 = Label(detail1, text=k10, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label10.grid(row=10, column=0)
    f_name_label11 = Label(detail1, text=k11, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label11.grid(row=11, column=0)
    f_name_label12 = Label(detail1, text=k12, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label12.grid(row=12, column=0)
    f_name_label13 = Label(detail1, text=k13, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label13.grid(row=13, column=0)
    f_name_label14 = Label(detail1, text=k14, font=('Helvetica', 10, 'bold'), bg="#1E0A4E", fg="white")
    f_name_label14.grid(row=14, column=0)

    fram2 = LabelFrame(detail11,text="OUR TEAM", bg="#1E0A4E", fg="white")
    fram2.grid(row=1, column=0, padx=10, pady=10, sticky=W+E)
    fram1 = LabelFrame(fram2, bg="#1E0A4E", fg="white")
    fram1.grid( padx=80, pady=10, sticky=W+E)

    label2 = Label(fram1, text="Sr. No.",font=('Helvetica',10,'bold'), bg="#1F77F9", fg="white")
    label2.grid(row=0, column=0, sticky=W)

    label3 = Label(fram1, text="Student Name (FULL)",font=('Helvetica',10,'bold'), bg="#1F77F9", fg="white")
    label3.grid(row=0, column=1, sticky=W)

    label4 = Label(fram1, text="Roll Number",font=('Helvetica',10,'bold'), bg="#1F77F9", fg="white")
    label4.grid(row=0, column=2, sticky=W)

    label5 = Label(fram1, text="System ID",font=('Helvetica',10,'bold'), bg="#1F77F9", fg="white")
    label5.grid(row=0, column=3, sticky=W)

    label6 = Label(fram1, text="1", bg="#1E0A4E", fg="white")
    label6.grid(row=1, column=0, sticky=W)

    label7 = Label(fram1, text="Seerat Musharaf", bg="#1E0A4E", fg="white")
    label7.grid(row=1, column=1, sticky=W)

    label8 = Label(fram1, text="200101284", bg="#1E0A4E", fg="white")
    label8.grid(row=1, column=2, sticky=W)

    label9 = Label(fram1, text="2020442638", bg="#1E0A4E", fg="white")
    label9.grid(row=1, column=3, sticky=W)

    label10 = Label(fram1, text="2", bg="#1E0A4E", fg="white")
    label10.grid(row=2, column=0, sticky=W)

    label11 = Label(fram1, text="Aakash Nakrami", bg="#1E0A4E", fg="white")
    label11.grid(row=2, column=1, sticky=W)

    label12 = Label(fram1, text="200101002", bg="#1E0A4E", fg="white")
    label12.grid(row=2, column=2, sticky=W)

    label13 = Label(fram1, text="2020000407", bg="#1E0A4E", fg="white")
    label13.grid(row=2, column=3, sticky=W)

    label14 = Label(fram1, text="3", bg="#1E0A4E", fg="white")
    label14.grid(row=3, column=0, sticky=W)

    label15 = Label(fram1, text="Harshit Kesharwani", bg="#1E0A4E", fg="white")
    label15.grid(row=3, column=1, sticky=W)

    label16 = Label(fram1, text="200101127", bg="#1E0A4E", fg="white")
    label16.grid(row=3, column=2, sticky=W)

    label17 = Label(fram1, text="2020508807", bg="#1E0A4E", fg="white")
    label17.grid(row=3, column=3, sticky=W)




splash.after(3000, main_window)

mainloop()

