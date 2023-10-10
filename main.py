from database import *

def add_test_values():
    insert_activity("Computing", "Necessity", 100, 0)
    insert_equipment("SSD", "Parts", "", "", 200, "", get_activity_id("Computing"))

    insert_activity("Producing", "Music", 50, 2)

    insert_activity("Longboarding", "Exercise", 20, 3)
    insert_equipment("Wheels", "Parts", "", "", 10, "2022-12-20", get_activity_id("Longboarding"))
    insert_expense("Repair", "Maintainance", "", "", 5.00, "2023-1-1", get_activity_id("Longboarding"))




if __name__ =="__main__":
    init_db()
    check_db()
    add_test_values()
    print(get_activities())
    print(get_equipment())
    print(get_expenses())
    close_db()
