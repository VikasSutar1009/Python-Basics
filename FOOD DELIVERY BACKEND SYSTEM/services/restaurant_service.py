from db.db_config import get_connection

def add_restaurant(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO restaurants(name) VALUES(%s)", (name))
    conn.commit()

def add_menu_item(restaurant_id, item_name, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO menu(restaurant_id, item_name, price) VALUES(%s,%s,%s)",
        (restaurant_id, item_name, price)
    )
    conn.commit()

def view_menu(restaurant_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT item_name, price FROM menu WHERE restaurant_id = %s",
        (restaurant_id,)
    )
    return cursor.fetchone()