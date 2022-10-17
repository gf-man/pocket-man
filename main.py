from database import * 

def add_test_values():
    insert_activity("Producing", "Music", 50, 0)
    insert_activity("Longboarding", "Exercise", 20, 0)







if __name__ =="__main__":
    init_db()
    check_db()
    add_test_values()
    print(get_activities())
    close_db()
