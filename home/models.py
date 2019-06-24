from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    id = models.UUIDField('Book Id',primary_key=True, default = uuid.uuid4, help_text="generated unique id for book")
    name = models.CharField(max_length=100, help_text='Book Name',null=True)
    purchase_date = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField('Genre', help_text='genre of book')
    book_author = models.ForeignKey('Author',on_delete=models.SET_NULL ,help_text='Book Author', null=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name +"- "+ self.book_author


class Author(models.Model):
    #id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=100, help_text='Name of Author',null=True)
    numChoice = (
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5','Five')
    )
    total_book_written = models.CharField(max_length=1,help_text='total_book_written',blank=True, choices=numChoice)
    date_of_birth = models.DateField(max_length=20,help_text='date_of_Birth',null=True, blank=True)
    date_of_death = models.DateField(max_length=20,help_text='date_of_Death',null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.author_name
        #return self.name +' (Written books - '+ self.book_author +')'

class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Book Name',null=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name