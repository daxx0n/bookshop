from django.db import models
from pathlib import Path
from PIL import Image
from django.urls import reverse_lazy
from directories.models import Author, Serie, Genre, Publisher
# Create your models here.
# 4.1.1. Название книги
# 4.1.2. Фото обложки
# 4.1.3. Цена (BYN)
# 4.1.4. Авторы книги (может содержать несколько авторов) - справочник
# 4.1.5  Серия - справочник
# 4.1.6. Жанры (один или несколько жанров) - справочник
# 4.1.7. Год издания
# 4.1.8. Страниц
# 4.1.9. Переплет
# 4.1.10. Формат
# 4.1.11. ISBN
# 4.1.12. Вес (гр)
# 4.1.13. Возрастные ограничения
# 4.1.14. Издательство - справочник
# 4.1.15. Количество книг в наличии
# 4.1.16. Активный (доступен для заказа, Да/Нет)
# 4.1.17. Рейтинг (0 - 10)
# 4.1.18. Дата внесения в каталог
# 4.1.19. Дата последнего изменения карточки
class Books(models.Model): 
    book_name = models.CharField(
        verbose_name="Book's name",
        max_length = 15,
        null = False,
        blank = False
    )
    picture = models.ImageField(
        verbose_name="Book picture",
        upload_to="uploads/%Y/%m/%d/"
    )
    book_price = models.DecimalField(
        verbose_name= "Book's price",
        decimal_places=2,
        max_digits=4
    )
    book_author = models.ForeignKey(
        "directories.Author", 
        verbose_name=("Author"), 
        blank = True,
        null = True,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return str(self.book_name)
 
    def get_absolute_url(self):
        return reverse_lazy ('directories:Success_Page')

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
                im.thumbnail ((m_basewidth ,hsize), Image.Resampling.LANCZOS)
                im.save(str(BASE_DIR / '.'.join(file_name[:-1])) + f'_{m_basewidth}_.' + extention)