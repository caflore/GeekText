from django.db import models

from books.models import Book
from users.models import User


class Rating(models.Model):
    rating = models.IntegerField() ##figure out how to min max the ratings
    comment = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE) ### setting to cascade in case book gets deleted, rating
                                                                ### should too
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) ### setting to do_nothing for now
    date = models.DateField()

    def __str__(self):
        return "Posted by: " + self.user.username + " Book: " + self.book.title