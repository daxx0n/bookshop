from django.db import models
from pathlib import Path
from PIL import Image
from directories import .

# Create your models here.
# Название книги
# 4.1.2. Фото обложки
# 4.1.3. Цена (BYN)
# 4.1.4. Авторы книги (может содержать несколько авторов) - справочник
# 4.1.5. Серия - справочник
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
        verbose_name="Book's name"
        max_length = 15,
        null = False,
        blank = False
    )
    picture = models.ImageField(
        verbose_name="Book picture",
        upload_to="uploads/%Y/%m/%d/"
    )
    price = models.DecimalField(
        verbose_name= "Book's price"
        max_digits=4
    )
    authors = models.ForeignKey(
        
    )