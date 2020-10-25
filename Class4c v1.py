from tkinter import ttk
import tkinter as tk
import pyodbc


#ConnectingDatabase#

from tkinter import messagebox
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MUTHUCOMPUTER;'
                      'Database=Class4c v1;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


#Adding new record#

def save():
    Names=   Name.get()
    Ages=    Age.get()
    Genders= Gender.get()
    Heights= height.get()
    weights= weight.get()
    rollnos= StudentId.get()
    Sports=Sport.get()

    cursor.execute("""
    INSERT INTO Students(Name, Age, Gender, Height,_weight,StudentId)
    VALUES (?,?,?,?,?,?)""",(Names,Ages,Genders,Heights,weights,rollnos))
    conn.commit()
    cursor.execute("""
    INSERT INTO Activity(Name,StudentId,Activity)
    VALUES (?,?,?)
    """,(Names,rollnos,Sports))
    conn.commit()
    clearfields()
    messagebox.showinfo("Tkinter", "Saved successfully!")


    
    
    













    
#deleting selected record and currently works only with rollnumber
        
        
def delete():
        x=StudentId.get()
        cursor.execute("""
        DELETE FROM Students
        WHERE StudentId = (?)""",(x))
        conn.commit()
        cursor.execute("""
        DELETE FROM Activity
        WHERE StudentId = (?)""",(x))
        clearfields()
        messagebox.showinfo("Tkinter", "Deleted successfully!")
        

#Searching records    

def Search():
 
        Names= Name.get()
        Ages= Age.get()
        Genders= Gender.get()
        Heights= height.get()
        Weights= weight.get()
        Rollnos= StudentId.get()
        Sports=Sport.get()

# clearing the tree
       
        t=tree.get_children()
        for f in t:
            tree.delete(f)
        

#Search starts
            

        if len(Names)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A._Weight,A.StudentId,B.Activity
            from Students A inner join Activity B on A.StudentId=B.StudentId where A.Name like(?)""",(Names))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)
                    
		
        elif  len(Ages)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A._Weight,A.StudentId,B.Activity
            from Students A inner join Sports B on A.StudentId=B.StudentId where A.Age like(?)""",(Ages))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(Genders)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A._Weight,A.StudentId,B.Activity
            from Students A inner join Sports B on A.StudentId=B.StudentId where A.Gender like(?)""",(Genders))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(Heights)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A._Weight,A.StudentId,B.Activity
            from Students A inner join Sports B on A.StudentId=B.StudentId where A.Height like(?)""",(Heights))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)          


        elif  len(Weights)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A._Weight,A.StudentId,B.Activity
            from Students A inner join Sports B on A.StudentId=B.StudentId where A._Weight like(?)""",(Weights))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(Rollnos)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A._Weight,A.StudentId,B.Activity
            from Students A inner join Sports B on A.StudentId=B.StudentId where A.StudentId like(?)""",(Rollnos))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(Sports)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A._Weight,A.StudentId,B.Activity
            from Students A inner join Sports B on A.StudentId=B.StudentId where B.Activity like(?)""",(Sports))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)

        else:
            
            messagebox.showinfo("Tkinter", "Atleast one search criteria must be given!")     

#Search ends

#  function to clear all entry fields

def clearfields():
    Name.delete(0 ,tk.END)
    Age.delete(0 ,tk.END)
    Gender.delete(0 ,tk.END)
    height.delete(0 ,tk.END)
    weight.delete(0 ,tk.END)
    StudentId.delete(0 ,tk.END)
    Sport.delete(0 ,tk.END)
    


       
# defining the canvas

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 900, height = 300)
canvas1.pack()

# Defining the fields and labels and validating

Name = tk.Entry (root)
canvas1.create_window(300, 10, window=Name)
label1 = tk.Label(root, text='Name:')
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 10, window=label1)


Age = tk.Entry (root)
canvas1.create_window(300, 40, window=Age)
label2 = tk.Label(root, text='Age:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 40, window=label2)

Gender = tk.Entry (root)
canvas1.create_window(300, 70, window=Gender)
label3 = tk.Label(root, text='Gender:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 70, window=label3)

height = tk.Entry (root)
canvas1.create_window(300, 100, window=height)
label4 = tk.Label(root, text='height in cm:')
label4.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label4)

weight = tk.Entry (root)
canvas1.create_window(300, 130, window=weight)
label5 = tk.Label(root, text='weight in kg:')
label5.config(font=('helvetica', 10))
canvas1.create_window(200, 130, window=label5)

StudentId = tk.Entry (root)
canvas1.create_window(300, 160, window=StudentId)
label6 = tk.Label(root, text='StudentId:')
label6.config(font=('helvetica', 10))
canvas1.create_window(200, 160, window=label6)

Sport = tk.Entry (root)
canvas1.create_window(300, 190, window=Sport)
label7 = tk.Label(root, text='Sport:')
label7.config(font=('helvetica', 10))
canvas1.create_window(200, 190, window=label7)


# Defining the buttons

button1 = tk.Button(text='Save',command = save)
canvas1.create_window(500, 250, window=button1)

button5 = tk.Button(text='Search',command=Search)
canvas1.create_window(400, 250, window=button5)

button3 = tk.Button(text='delete',command=delete)
canvas1.create_window(450, 250, window=button3)

# Defining the tree

tree=ttk.Treeview(root)
tree["columns"]=("one","two","three","four","five","six")
tree.column("#0", width=130, minwidth=270, stretch=tk.NO)
tree.column("one", width=100, minwidth=150, stretch=tk.NO)
tree.column("two", width=100, minwidth=100)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("one", text="Age",anchor=tk.W)
tree.heading("two", text="Gender",anchor=tk.W)
tree.heading("three", text="Height",anchor=tk.W)
tree.heading("four", text="Weight",anchor=tk.W)
tree.heading("five", text="StudentId",anchor=tk.W)
tree.heading("six", text="Sports",anchor=tk.W)
tree.pack()
root.mainloop()
