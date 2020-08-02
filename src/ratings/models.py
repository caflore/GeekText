from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from books.models import Book
from users.models import User


class Rating(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return "Posted by: " + self.user.username + " Book: " + self.book.title