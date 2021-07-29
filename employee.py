import sqlite3
db = sqlite3.connect("employ.db")
cr = db.cursor()
cr.execute("Create table if not exists emp(id_num integer, name text , position text,salary float)")

def check(a):
    cr.execute(F"select id_num from emp where {a} == id_num")
    if len(cr.fetchall())!=0:
        return True
    else:
        return False


def add():
    """
    add an employee to the database
    """
    print("give the id of the employee:")
    o = int(input(">"))
    while check(o):
        print("this id already exists")
        print("give the id of the employee:")
        o = int(input(">"))

    else:
        print("give the name of employee:")
        u = input(">")
        print("give the position of employee:")
        p = input(">")
        print("give the salary of employee:")
        q = float(input(">"))
        cr.execute(f"insert into emp(id_num,name,position,salary) values({o},'{u}','{p}',{q})")
        db.commit()
        print("succefully added to database")



def delete():
    """
    delete an employee from the database
    """
    print("give the id of the employee:")
    o = int(input(">"))
    while check(o)!=True:
        print("give the id of the employee:")
        o = int(input(">"))
        print("this id doesn't exists")
    cr.execute(f"delete from emp where id_num == {o}")
    db.commit()
    print("succefully deleted")

def update():
    """
    update the infos of an employee
    """
    print("give the id of the employee:")
    o = int(input(">"))
    while check(o)!=True:
        print("give the id of the employee:")
        o = int(input(">"))
        print("this id doesn't exists")
    print("type the new name or type -1 if you don't want to update it: ")
    k = input(">")
    if k != "-1":
        cr.execute(f"update emp set name == '{k}' where id_num == {o}  ")
    else:
        pass


    print("type the new position or type -1 if you don't want to update it: ")
    k = input(">")
    if k != "-1":
        cr.execute(f"update emp set position == '{k}' where id_num == {o}  ")
    else:
        pass
    print("type the new salary or type -1 if you don't want to update it: ")
    k = input(">")
    if k != "-1":
        k = float(k)
        cr.execute(f"update emp set salary == '{k}' where id_num == {o}  ")
    else:
        pass
    db.commit()

def get(sal):
    """
    return the employees who has more than this salary and less
    """
    cr.execute(f"select * from emp where {sal}<=salary")
    k = cr.fetchall()
    if  len(k)!=0:
        print(f"the employees who have more than {sal} in salary are:")
        print(k)
    else:
        print(f"there is no employee who has this {sal} or more than it")

    cr.execute(f"select * from emp where {sal}>salary")
    k = cr.fetchall()
    if len(k)!=0:
        print(f"the employees who has less than {sal} in salary are:")
        print(k)
    else:
        print(f"there is no employee who has this {sal} ")


def clear():

   """
   delete all the employees
   """
   k = 1
   cr.execute(f"delete from emp where {k}")
   db.commit()
   print("deleted succefully")





def getbypos():
    print("give a position to get all the employees who have this position:")
    d = input(">")
    cr.execute(f"select * from emp where position is '{d}'")
    k = cr.fetchall()
    if  len(k)!=0:
        print(f"the employees who has the position  {d} are:")
        print(k)
    else:
        print(f"there is no employee who has this position  {d} .")


con = True

while con  :
    print("welcome to my app")
    print("you have 5 options")
    print("1- add an employee .")
    print("2- update an employee .")
    print("3- delete an employee .")
    print("4- get employees who have more and less than an input salary .")
    print("5- get employees with an input position .")
    print("6- delete all the employees.")
    print("7- quit the app")
    print("type a valid input:")
    choice = int(input(">"))
    while choice < 1 or choice > 7:
        print("type a valid input:")
        choice = int(input(">"))

    if choice == 1:
        add()
    elif choice == 2:
        update()
    elif choice == 3:
        delete()
    elif choice == 4:
        print("give a salary:")
        d = float(input())
        get(d)
    elif choice == 5:
        getbypos()
    elif choice == 6:
        clear()
    else:
        con = False

print("app closed")
print("thanks for using our app")
