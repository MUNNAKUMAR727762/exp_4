import sqlite3
con=sqlite3.connect('Student.db')


def insertData (Name, Company, Salary, ID):
    qry="insert into Student (Name, ID, Company, Salary) values (?,?,?,?);" 
    con.execute(qry, (Name, Company, Salary,ID)) 
    con.commit() 
    print("User Details Added")
    
    
def updateData (Name, Company, Salary, id):
    qry="update users set Name=?, Name=?, Company=?, Salary=?, where id=?;" 
    con.execute(qry, (Name, Company, Salary, id)) 
    con.commit()
    print("User Details Updated")
    
    
def deleteData(id): 
    qry="delete from users where id=?;" 
    con.execute(qry, (id)) 
    con.commit() 
    print("User Details Deleted")
    
    
def selectData():
    qry="select * from Student"
    result=con.execute(qry)
    for row in result:
        print(row)
        
    print("""1.Insert
          2.Update 
          3.Delete 
          4.Select""")
          
          
ch=1
while ch==1:
    c=int(input("Select Your Choice: "))
    if(c==1):
        print("Add New Record")
        Name=input("Enter Name: ")
        ID=input("Enter ID: ")
        Company=input("Enter Company: ")
        Salary=input("Enter Salary: ")
        insertData(Name, Company, Salary,ID)
    elif (c==2):
        print("Edit A Record") 
        id=input("Enter ID: ")
        Name=input("Enter Name: ")
        # ID=input("Enter ID: ")
        Company=input("Enter Company : ") 
        Salary=input("Enter Salary: ")
        updateData(Name, Company, Salary,id)
    elif (c==3):
        print("Delete A Record") 
        id=input("Enter ID: ")
        deleteData(id)
    elif (c==4):
        print("Print All Record") 
        selectData()
    else:
        print("Invalid Selectio") 
        ch=int(input("Enter 1 To Continue: "))
print("Thank You")