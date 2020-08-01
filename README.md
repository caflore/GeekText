# GeekText
CEN 4010 Group Project

Admin:
  - Username: root
  - Password: toor

Using:
  - Python 3.7.5 virtualenv


# Quick git tutorials:
  - https://git-scm.com/docs/gittutorial

  - https://www.youtube.com/watch?v=0fKg7e37bQE

# Sample Requests #

  ## User Profile (Carlos Flores) ##

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


  ## Book Details ##

  - Add book to database (POST)
  - http://127.0.0.1:8000/books/

  ```JSON
  {
    "title": "",
    "book_ISBN": "",
    "price": null,
    "genre": "",
    "yearPublished": null,
    "copiesSold": null,
    "publisher": "",
    "description": "",
    "author": null
  }
  ```
  - Get book by ISBN (GET)
  - http://127.0.0.1:8000/books/?book_ISBN=9780307743657

  - Create Author (POST)
  - http://127.0.0.1:8000/author/

  ```JSON
  {
    "fName": "",
    "lName": "",
    "biography": "",
    "publisher": ""
  }
  ```
  ## Book Browsing and Sorting ##

  - Retrieve List of Books by Genre (GET)
  - http://127.0.0.1:8000/books/?genre=Fantasy

  - Retrieve List of Top Sellers (Top 10 books that have sold the most copied) (GET)
  - http://127.0.0.1:8000/books/top_sellers/

  - Retrieve List of Books for a particular rating and higher (GET)
  - http://127.0.0.1:8000/books/top_rated/?rating=1

  - Retrieve List of X Books at a time where X is an integer (GET)
  - http://127.0.0.1:8000/books/top_x/?count=2

  ## Ratings and Comments ##
    
  - Create rating on a 5-star scale with datestamp
    
  - Create a comment with a datestamp
  ```JSON
  {
      "rating": 5,
      "comment": "This is a great book",
      "date": "2020-08-02",
      "book": "http://127.0.0.1:8000/books/3/",
      "user": "http://127.0.0.1:8000/users/1/"
  }
  ```
  
   - Retrieve a list of ratings and comments sorted by top rated
   - http://127.0.0.1:8000/rating/top_ratings/  
   
   - Retrieve average rating for a book
   - http://127.0.0.1:8000/books/avg_book_rating/?ISBN=9780307743657
