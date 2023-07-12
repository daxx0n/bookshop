from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from proj.services.utils import unique_slugify



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='images/avatars/%Y/%m/%d/', 
        default='images/avatars/default.jpg',
        blank=True,  
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    phone = models.CharField (null=False, blank=False, verbose_name='Телефон', max_length=12, default="")
    country = models.CharField (null=True, blank=True, verbose_name='Страна', max_length=15)
    city = models.CharField (null=True, blank=True, verbose_name='Город', max_length=15)
    index = models.IntegerField (null=True, blank=True, verbose_name='Индекс')
    address_1 = models.CharField (null=True, blank=True, verbose_name='Адрес1', max_length=30)
    address_2 = models.CharField (null=True, blank=True, verbose_name='Адрес2', max_length=30)
    other = models.TextField(max_length=500, blank=True, verbose_name='Дополнительная информация')
    

    

    class Meta:
        db_table = 'app_profiles'
        ordering = ('user',)
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Возвращение строки
        """
        return self.user.username
    
    def get_absolute_url(self):
        """
        Ссылка на профиль
        """
        return reverse('staff:profile_detail', kwargs={'slug': self.slug})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()