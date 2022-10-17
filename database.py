import sqlite3

def init_db():
    try:
        global db, cur
        db = sqlite3.connect("./pocket_man.db")
        cur = db.cursor()
    except:
        print("error loading db")
        raise

def create_db():
    with open("./create_db.sql", "r") as sql_file:
        cur.executescript(sql_file.read())

def check_db():
    cur.execute("SELECT NAME FROM SQLITE_MASTER")
    if cur.fetchall() == []:
        if input("Press Y to create a new db file:\n").upper() == "Y":
            create_db()

def commit_to_db():
    db.commit()

def close_db():
    try:
        cur.close()
        db.commit()
        db.close()
    except:
        print("error closing db")
        raise

# CRUD Variables (Create, Read, Update, Delete)
def insert_variable(name, value):
    query = '''
    insert into Variables (Name, Value)
    values (?, ?)
    '''
    cur.execute(query, (name, value)) 

def get_variables():
    query = '''
    select VarId, Name, Value
    from Variables'''
    return cur.execute(query).fetchall()

def get_variable_id(name):
    query = '''
    select VarId 
    from Variables where Name is ?'''
    return cur.execute(query, (name,)).fetchall()[0][0]

def get_variable_name(varId):
    query = '''
    select Name
    from Variables where VarId is ?'''
    return cur.execute(query, (name,)).fetchall()[0][0]

def get_variable_details(varId):
    query = '''
    select VarId, Name, Value
    from Variables where VarId is ?'''
    return cur.execute(query, (varId,)).fetchall()

def update_variable(varId, name=None, value=None):
    query = '''
    update Variables
    set Name=?, Value=?
    where id is ?'''
    data = get_variable_details(varId)
    if not name: name = data[1]
    if not value: value = data[2]
    cur.execute(query, (name, value))

def remove_variable(varId):
    query = '''
    delete 
    from Variables where VarId is ?'''
    cur.execute(query, (varId))


# CRUD Income (Create, Read, Update, Delete)
def insert_income(name, category, amount, payInDate, inId):
    query = '''
    insert into Income (Name, Category, Amount, PayInDate, ActId)
    values (?, ?, ?, ?, ?)
    '''
    cur.execute(query, (name, category, amount, payInDate, inId))

def get_incomes():
    query = '''
    select InId, Name, Category, Amount, PayInDate, ActId
    from Income'''
    return cur.execute(query).fetchall()

def get_income_id(name):
    query = '''
    select InId 
    from Income where Name is ?'''
    return cur.execute(query, (name,)).fetchall()[0][0]

def get_income_name(inId):
    query = '''
    select Name
    from Income where InId is ?'''
    return cur.execute(query, (name,)).fetchall()[0][0]

def get_income_details(inId):
    query = '''
    select InId, Name, Category, Amount, PayInDate, ActId
    from Income where InId is ?'''
    return cur.execute(query, (inId,)).fetchall()

def update_income(inId, name=None, category=None, amount=None, payInDate=None, actId=None):
    query = '''
    update Income
    set Name=?, Category=?, Amount=?, PayInDate=?, ActId=?
    where id is ?'''
    data = get_income_details(inId)
    if not name: name = data[1]
    if not category: category = data[2]
    if not amount: amount = data[3]
    if not payInDate: payInDate = data[4]
    if not actId: actId = data[5]
    cur.execute(query, (name, category, budget, priority, inId))

def remove_income(inId):
    query = '''
    delete 
    from Income where InId is ?'''
    cur.execute(query, (inId))


# CRUD Activity (Create, Read, Update, Delete)
def insert_activity(name, category, budget, priority):
    query = '''
    insert into Activity (Name, Category, Budget, Priority)
    values (?, ?, ?, ?)
    '''
    cur.execute(query, (name, category, budget, priority))

def get_activities():
    query = '''
    select ActId, Name, Category, Budget, Priority
    from Activity'''
    return cur.execute(query).fetchall()

def get_activity_id(name):
    query = '''
    select ActId 
    from Activity where Name is ?'''
    return cur.execute(query, (name,)).fetchall()[0][0]

def get_activity_name(actId):
    query = '''
    select Name
    from Activity where ActId is ?'''
    return cur.execute(query, (name,)).fetchall()[0][0]

def get_activity_details(actId):
    query = '''
    select ActId, Name, Category, Budget, Priority
    from Activity where ActId is ?'''
    return cur.execute(query, (actId,)).fetchall()

def update_activity(actId, name=None, category=None, budget=None, priority=None):
    query = '''
    update Activity
    set Name=?, Category=?, Budget=?, Priority=?
    where id is ?'''
    data = get_activity_details(actId)
    if not name: name = data[1]
    if not category: category = data[2]
    if not budget: budget = data[3]
    if not priority: priority = data[4]
    cur.execute(query, (name, category, budget, priority, actId))

def remove_activity(actId):
    query = '''
    delete 
    from Activity where ActId is ?'''
    cur.execute(query, (actId))



# CRUD Expense (Create, Read, Update, Delete)
def insert_expense(name, category, url, desc, cost, payOutDate, actId):
    query = '''
    insert into Expense (Name, Category, URL, Description, Cost, PayOutDate, ActId)
    values (?, ?, ?, ?, ?, ?, ?)
    '''
    cur.execute(query, (name, category, url, desc, cost, payOutDate, actId))

def get_expenses():
    query = '''
    select ExId, Name, Category, URL, Description, Cost, PayOutDate, ActId
    from Expense'''
    return cur.execute(query).fetchall()

def get_expense_id(name):
    query = '''
    select ExId 
    from Expense where Name is ?'''
    return cur.execute(query, (name,)).fetchall()[0][0]

def get_expense_name(exId):
    query = '''
    select Name
    from Expense where ExId is ?'''
    return cur.execute(query, (name,)).fetchall()[0][0]

def get_expense_details(exId):
    query = '''
    select ExId, Name, Category, URL, Description, Cost, PayOutDate, ActId
    from Expense where ExId is ?'''
    return cur.execute(query, (exId,)).fetchall()

def update_expense(eqId, name=None, category=None, url=None, desc=None, cost=None, payOutDate=None, actId=None):
    query = '''
    update Expense
    set Name=?, Category=?, URL=?, Description=?, Cost=?, PayOutDate=?, ActId=?))
    where id is ?'''
    data = get_eqpense_details(eqId)
    if not name: name = data[1]
    if not category: category = data[2]
    if not url: url = data[3]
    if not desc: desc = data[4]
    if not cost: cost = data[5]
    if not payOutDate: payOutDate = data[6]
    if not actId: actId = data[7]
    cur.execute(query, (name, category, url, desc, cost, payOutDate, actId))

def remove_expense(exId):
    query = '''
    delete 
    from Expense where ExId is ?'''
    cur.execute(query, (exId))


# CRUD Equipment (Create, Read, Update, Delete)
def insert_equipment(name, category, url, desc, cost, payOutDate, actId):
    query = '''
    insert into Equipment (Name, Category, URL, Description, Cost, PayOutDate, ActId)
    values (?, ?, ?, ?, ?, ?, ?)
    '''
    cur.execute(query, (name, category, url, desc, cost, payOutDate, actId))

def get_equipment():
    query = '''
    select EqId, Name, Category, URL, Description, Cost, PayOutDate, ActId
    from Equipment'''
    return cur.execute(query).fetchall()

def get_equipment_id(name):
    query = '''
    select EqId 
    from Equipment where Name is ?'''
    return cur.execute(query, (name,)).fetchall()[0][0]

def get_equipment_name(eqId):
    query = '''
    select Name
    from Equipment where ActId is ?'''
    return cur.execute(query, (name,)).fetchall()[0][0]

def get_equipment_details(eqId):
    query = '''
    select EqId, Name, Category, URL, Description, Cost, PayOutDate, ActId
    from Equipment where EqId is ?'''
    return cur.execute(query, (eqId,)).fetchall()

def update_equipment(eqId, name=None, category=None, url=None, desc=None, cost=None, payOutDate=None, actId=None):
    query = '''
    update Equipment
    set Name=?, Category=?, URL=?, Description=?, Cost=?, PayOutDate=?, actId=?))
    where id is ?'''
    data = get_equipment_details(eqId)
    if not name: name = data[1]
    if not category: category = data[2]
    if not url: url = data[3]
    if not desc: desc = data[4]
    if not cost: cost = data[5]
    if not payOutDate: payOutDate = data[6]
    if not actId: actId = data[7]
    cur.execute(query, (name, category, url, desc, cost, payOutDate, actId))

def remove_equipment(eqId):
    query = '''
    delete 
    from Equipment where EqId is ?'''
    cur.execute(query, (eqId))

