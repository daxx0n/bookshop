from django.db import models

# Create your models here.

class Author(models.Model):
    author_firstname = models.CharField(
            verbose_name = 'Author Name',
            max_length = 15,
            null = False,
            blank = False,
            default = "Author's firstname"
    )
    author_lastname = models.CharField(
            verbose_name = 'Author Lastname',
            max_length=15,
            null = False,
            blank = False,
            default = "Author's lastname"
    )
    def __str__(self):
        return str(self.author_lastname)+ " " + str(self.author_firstname[0]+ ".")

class Serie(models.Model):
    serie_name = models.CharField(
            verbose_name = 'Serie',
            max_length = 40,
            null = False,
            blank = False,
            default = "Serie name"
    )
    serie_description = models.TextField(
            verbose_name ='Serie description',
            max_length = 255,
            null = True,
            blank = True  
    )  
    def __str__(self):
        return (self.serie_name)
    
class Genre(models.Model):
    genre_name = models.CharField(
            verbose_name = 'Genre',
            max_length = 30,
            null = False,
            blank = False,
            default="Genre name"
    )
    genre_description = models.TextField(
            verbose_name = 'Genre description',
            max_length = 255,
            null = True,
            blank = True
    )
    def __str__(self):
        return (self.genre_name)
    
class Publisher(models.Model):
    publisher_name = models.CharField(
            verbose_name = 'Publisher',
            max_length = 30,
            null = False,
            blank = False,
            default = "Publisher's name"
    )
    publisher_description = models.TextField(
            verbose_name = 'Publisher description',
            max_length = 255,
            null=True,
            blank=True
    )
    def __str__(self):
        return (self.publisher_name)