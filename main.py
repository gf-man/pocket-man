import sqlite3

global db, cur
db, cur = None, None

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


# CRUD Income (Create, Read, Update, Delete)
def insert_income(name, category, amount, payInDate, actId):
    query = '''
    insert into Income (Name, Category, Amount, PayInDate, ActId)
    values (?, ?, ?, ?, ?)
    '''
    cur.execute(query, (name, category, amount, payInDate, actId))

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

def get_income_name(actId):
    query = '''
    select Name
    from Income where InId is ?'''
    return cur.execute(query, (name,)).fetchall()[0][0]

def get_income_details(actId):
    query = '''
    select InId, Name, Category, Amount, PayInDate, ActId
    from Income where InId is ?'''
    return cur.execute(query, (actId,)).fetchall()

def update_income(actId, name=None, category=None, amount=None, payInDate=None, ActId=None):
    query = '''
    update Income
    set Name=?, Category=?, Amount=?, PayInDate=?, ActId=?
    where id is ?'''
    data = get_income_details(actId)
    if not name: name = data[1]
    if not category: category = data[2]
    if not amount: amount = data[3]
    if not payInDate: payInDate = data[4]
    if not ActId: ActId = data[5]
    cur.execute(query, (name, category, budget, priority, actId))

def remove_income(actId):
    query = '''
    delete 
    from Income where InId is ?'''


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













if __name__ =="__main__":
    init_db()
    check_db()
    insert_activity("Producing", "Music", 50, 0)
    insert_activity("Longboarding", "Exercise", 20, 0)
    print(get_activity_id("Longboarding"))
    print(get_activity_details(1))
    close_db()
