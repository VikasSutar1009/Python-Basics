from db.db_config import get_connection
from services.payment_service import process_payment
from services.logger_service import log_event
from services.cache_service import cache_get, cache_set


def update_order_status(order_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE orders SET status = %s WHERE order_id = %s",
        (status, order_id)
    )

    conn.commit()
    log_event(f"Order {order_id} status updated to {status}")

def place_order(user_id, *items):
    conn = get_connection()
    cursor = conn.cursor()

    total = sum([item[1] for item in items])

    def get_order(order_id):
        cached = cache_get(f"order: {order_id}")
        if cached:
            return cached
        
        # DB fetch (pseudo)
        order = {"order_id": order_id, "status": "DELIVERED"}
        cache_set(f"order:{order_id}", order)

        return order
    

    # --------------PAYENT STEP -------------
    payment = process_payment(user_id, total)

    if payment["status"] != "SUCCESS":
        log_event("Payment Failed ")
        return
    
    # --------------ORDER SAVED AFTER PAYMENT -----------
    cursor.execute(
        "INSERT INTO orders(user_id, total_amount) VALUES(%s,%s)",
        (user_id, total)
    )

    order_id = cursor.lastrowid

    for item in items:
        cursor.execute(
            "INSERT INTO order_items(order_id, item_name, price) VALUES(%s,%s,%s)",
            (order_id, item[0], item[1])
        )

    update_order_status(order_id, "PAID")
    log_event("Order {order_id} placed successfully")

    return order_id