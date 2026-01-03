from services.order_service import place_order

def test_place_order():
    result = place_order(1, ("Pizza", 200))
    assert result is not None