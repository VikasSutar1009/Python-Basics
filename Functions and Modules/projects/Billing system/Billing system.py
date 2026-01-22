def calculate_bill(*prices):
    total = sum(prices)
    gst = total +0.18
    return total + gst

bill = calculate_bill(200, 150,300)