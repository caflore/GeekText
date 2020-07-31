# GeekText
CEN 4010 Group Project

Admin:
  - Username: root
  - Password: toor

Using:
  - Python 3.7.5 virtualenv

Markup :  - - - -

# Quick git tutorials:
  - https://git-scm.com/docs/gittutorial

  - https://www.youtube.com/watch?v=0fKg7e37bQE

# Sample Requests #

  ## User Profile ##

  - Get user list (GET)
  - http://127.0.0.1:8000/users/

  - Create user (POST)
  - http://127.0.0.1:8000/users/
  ```JSON
  {
    "username": "",
    "password": "",
    "email": "",
    "first_name": "",
    "last_name": "",
    "address": "",
    "zip_code": "",
    "city": "",
    "country": ""
  }
  ```

  - User search by username (GET)
  - http://127.0.0.1:8000/users/?username=cflor

  - Update user (PUT/PATCH)
  - http://127.0.0.1:8000/users/4/
  ```JSON
  {
    "url": "http://127.0.0.1:8000/users/4/",
    "id": 4,
    "username": "cflor",
    "email": null,
    "first_name": "Carlos",
    "last_name": "Flores",
    "address": "",
    "zip_code": "",
    "city": "",
    "country": ""
  }
  ```
  - Get creditcard list (GET)
  - http://127.0.0.1:8000/creditcards/

  - Create credit card (POST)
  - http://127.0.0.1:8000/creditcards/
  ```JSON
  {
    "creditcard_number": "986857648242",
    "user": "http://127.0.0.1:8000/users/1/"
  }
  ```

  - Get cards for user (GET)
  - http://127.0.0.1:8000/creditcards/?search=root

  ## Shopping Cart ##

  - Cart is created when user is created.

  - Add book to shopping cart (POST)
  - http://127.0.0.1:8000/shopping_cart_items/
  ```JSON
  {
        "quantity": 1,
        "cart": "http://127.0.0.1:8000/shopping_cart/1/",
        "item_id": "http://127.0.0.1:8000/books/3/"
  }
  ```
  - Search cart items for user (GET)
  - http://127.0.0.1:8000/shopping_cart_items/?search=cflor

  - Delete book from cart (DELETE)
  - http://127.0.0.1:8000/shopping_cart_items/3/


  ```JSON

  ```
  ```JSON

  ```
  ```JSON

  ```
  ```JSON

  ```
  ```JSON

  ```
