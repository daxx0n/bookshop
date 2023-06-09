from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from pathlib import Path
from django.utils import timezone
from PIL import Image
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Books(models.Model): 
    
    book_name = models.CharField(
        verbose_name="Book's name",
        max_length = 40,
        null = False,
        blank = False
    )
    picture = models.ImageField(
        verbose_name="Book picture",
        upload_to="uploads/%Y/%m/%d/",
        default='images/default_book.png',
        blank=True
    )
    book_price = models.DecimalField(
        verbose_name= "Book's price",
        decimal_places=2,
        max_digits=6,
        validators=[MinValueValidator(0)]
    )
    book_author = models.ForeignKey(
        "directories.Author", 
        verbose_name=("Author"), 
        blank = True,
        null = True,
        on_delete=models.CASCADE
    )
    book_serie = models.ForeignKey(
        "directories.Serie", 
        verbose_name=("Serie"), 
        blank = True,
        null = True,
        on_delete=models.CASCADE
    )
    book_genre = models.ForeignKey(
        "directories.Genre", 
        verbose_name=("Genre"), 
        blank = True,
        null = True,
        on_delete=models.CASCADE
    )
    book_year = models.PositiveIntegerField(
        verbose_name=("Year"), 
        blank = True,
        null = True,
        validators=[MaxValueValidator(2023)]
    )
    book_page = models.PositiveIntegerField(
        verbose_name=("Pages"), 
        blank = True,
        null = True
    )
    COVER_BOOK = (
        ('M', 'мягкая'),
        ('T', 'твердая'),
    )
    book_cover = models.CharField(
        verbose_name=("Cover"),
        max_length = 5,
        choices= COVER_BOOK,
        default= "M"
    )
    book_isbn = models.CharField(
        verbose_name=("ISBN"), 
        max_length = 17,
        blank = True,
        null = True
    )
    book_weight = models.PositiveIntegerField(
        verbose_name=("Weight"), 
        blank = True,
        null = True,
        validators=[MinValueValidator(1)]
    )
    book_age = models.CharField(
        verbose_name=("Age Restrictions"), 
        max_length = 3,
        blank = True,
        null = True
    )
    book_publisher = models.ForeignKey(
        "directories.Publisher", 
        verbose_name=("Publisher"), 
        blank = True,
        null = True,
        on_delete=models.CASCADE
    )
    book_quantity = models.PositiveIntegerField(
        verbose_name=("Book quantity"), 
        blank = True,
        null = True
    )
    ISACTIVE = (
        ('Y', 'активна'),
        ('N', 'не активна'),
    )
    is_active = models.CharField(
        verbose_name = 'Book active',
        max_length = 4,
        choices = ISACTIVE
    )
    
    book_rating = models.DecimalField( 
        verbose_name=("Book rating"),
        max_digits=4,
        decimal_places=2, 
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    created_at = models.DateTimeField(
        auto_now_add=True)
    
    updated_at = models.DateTimeField(
        auto_now=True
        )
    

    def __str__(self):
        return str(self.book_name)
 
    def get_absolute_url(self):
        return reverse_lazy ('directories:Success_Page')
    
    def get_search_url_books(self):
        return f"/books/book_view/{self.pk}"

    def book_picture_med (self):
        original_url = self.picture.url
        new_url = original_url.split('.')
        picture_url = ".".join(new_url[:-1]) + "_150_." + new_url[-1]
        return picture_url

    def book_picture_small (self):
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
                im.thumbnail ((m_basewidth,hsize), Image.Resampling.LANCZOS)
                im.save(str(BASE_DIR / '.'.join(file_name[:-1])) + f'_{m_basewidth}_.' + extention)
    
class Comments(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name = 'comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.book, self.user)
