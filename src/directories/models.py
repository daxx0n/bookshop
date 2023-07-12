from pathlib import Path
from django.db import models
from django.urls import reverse_lazy
from PIL import Image

# Create your models here.

class Author(models.Model): 
    picture = models.ImageField(
            verbose_name="Author picture",
            upload_to="uploads/%Y/%m/%d/"
    )
    author_firstname = models.CharField(
            verbose_name = 'Author Name',
            max_length = 15,
            null = False,
            blank = False,
            default = "Author's firstname",
            help_text= "Add Author's name, max len = 15"
    )
    author_lastname = models.CharField(
            verbose_name = 'Author Lastname',
            max_length=15,
            null = False,
            blank = False,
            default = "Author's lastname",
            help_text= "Add Author's lastname, max len = 15"
    )
    author_bio = models.TextField(
            verbose_name = 'Author Bio',
            max_length=1000,
            null = True,
            blank = True,
            help_text= "Author's biography, max len = 300"
    )
    def __str__(self):
        return str(self.author_lastname)+ " " + str(self.author_firstname)
 
    def get_absolute_url(self):
        return reverse_lazy ('Home Page')

    def get_search_url_author(self):
        return f"/directories/author_view/{self.pk}"

    def author_picture_med (self):
        original_url = self.picture.url
        new_url = original_url.split('.')
        picture_url = ".".join(new_url[:-1]) + "_150_." + new_url[-1]
        return picture_url

    def author_picture_small (self):
        original_url = self.picture.url
        new_url = original_url.split('.')
        picture_url = ".".join(new_url[:-1]) + "_40_." + new_url[-1]
        return picture_url

    def picture_resizer (self):
        extention = self.picture.file.name.split('.')[-1]
        BASE_DIR = Path(self.picture.file.name).resolve().parent
        file_name = Path(self.picture.file.name).resolve().name.split('.')
        for m_basewidth in [150, 40]:
                im = Image.open(self.picture.file.name)
                wpercent = (m_basewidth/float(im.size[0]))
                hsize = int((float(im.size[1])*float(wpercent)))
                im.thumbnail ((m_basewidth ,hsize), Image.Resampling.LANCZOS)
                im.save(str(BASE_DIR / '.'.join(file_name[:-1])) + f'_{m_basewidth}_.' + extention)
    
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

    def get_absolute_url(self):
        return reverse_lazy ('directories:Success_Page')
    
    def get_search_url_serie(self):
        return f"/directories/serie_view/{self.pk}"
    
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

    def get_absolute_url(self):
        return reverse_lazy ('directories:Success_Page')

    def get_search_url_genre(self):
        return f"/directories/genre_view/{self.pk}"
    
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

    def get_absolute_url(self):
        return reverse_lazy ('directories:Success_Page')
    
    def get_search_url_publisher(self):
        return f"/directories/publisher_view/{self.pk}"