from django.db import models


class Author(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    biography = models.TextField()
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.fName + ' ' + self.lName


class Book(models.Model):
    title = models.CharField(max_length=120)
    book_ISBN = models.CharField(max_length=20, unique=True, null=False)
    price = models.FloatField()
    genre = models.CharField(max_length=20)
    yearPublished = models.IntegerField()
    copiesSold = models.IntegerField(default=0)
    publisher = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title
