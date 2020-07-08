from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 120)
    book_ISBN = models.CharField(max_length = 20, unique = True, null = False)
    price = models.FloatField()
    genre = models.CharField(max_length = 20)
    yearPublished = models.IntegerField()
    copiesSold = models.IntegerField(default = 0)
    publisher = models.CharField(max_length = 120)
    authorID = models.CharField(max_length = 20, unique = True, null = false)
    description = models.TextField()

    def __str__(self):
        return self.title




