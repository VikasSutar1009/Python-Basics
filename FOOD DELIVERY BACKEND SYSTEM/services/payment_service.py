import random
import time

def process_payment(user_id, amount, method = 'UPI'):
    print("\n--- PAYMENT GATEWAY ---")
    print(f"Payment Method: {method}")
    print(f"Amount to Pay: {amount}")

    # Simulate payment processing dekay
    time.sleep(2)

    # Simulate success / failure
    payment_status = random.choice(["SUCCESS", "FAILED"])

    if payment_status == "SUCCESS":
        transaction_id  = "TXN"+ str(random.randint(10000, 99999))
        print("Payment Successful")
        print("Transaction ID:", transaction_id)
        return{
            "status": "SUCCESS",
            "transaction_id": transaction_id
        }
    else:
        print("Payment Failed")
        return{
            "status": "FAILED",
            "transaction_id": None
        }