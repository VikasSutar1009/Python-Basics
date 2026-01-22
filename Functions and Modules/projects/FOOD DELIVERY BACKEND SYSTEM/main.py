from services.user_service import register_user, login_user
from services.restaurant_service import add_restaurant, add_menu_item,view_menu
from services.order_service import place_order
from services.auth_service import verify_token

# Register User
register_user(name = "Rahul", email = "rahul@gmail.com", password = "1234")

# Login
token = login_user("rahul@gmail.com", "1234")


if not token:
    print("Login Failed")
    exit()


print("JWT Token", token)

user_id = verify_token(token)


if user_id:
    add_restaurant("Dominos")
    add_menu_item(1, "Pizza", 250)
    add_menu_item(1, "Burger", 150)

    menu = view_menu(1)
    print("Menu:",menu)

    place_order(
        user_id,
        ("Pizza", 250),
        ("Burger", 150)
    )