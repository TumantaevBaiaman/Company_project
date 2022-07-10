from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    img = models.ImageField(verbose_name='Фото категории', upload_to='post_image')
    name = models.CharField(max_length=25, verbose_name='Название')
    content = models.TextField(verbose_name='Подробнее')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']


class Licenses(models.Model):
    licenses = models.CharField(max_length=255, verbose_name='Лицензи')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.licenses

    def get_absolute_url(self):
        return reverse('detail_l', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Лицензия'
        verbose_name = 'Лицензи'
        ordering = ['licenses']


class Forma(models.Model):
    forma = models.CharField(max_length=255, verbose_name='форма')

    def __str__(self):
        return self.forma

    def get_absolute_url(self):
        return reverse('detail_f', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Форма'
        verbose_name = 'Форма'
        ordering = ['forma']


class Comment(models.Model):
    comment = models.TextField(verbose_name="Комментарии")

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('detail_k', kwargs={'pk': self.pk})


class Info(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото компании')
    num = models.CharField(max_length=255, verbose_name='ИНН')
    admin = models.CharField(max_length=255, verbose_name='Администратор')
    country = models.CharField(max_length=255, verbose_name='Гражданин')
    contact = models.CharField(max_length=255, verbose_name='Номер')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категории')
    licenses = models.ForeignKey(Licenses, on_delete=models.CASCADE, verbose_name='Лицензи')
    forma = models.ForeignKey(Forma, on_delete=models.CASCADE, verbose_name='форма')
    content = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Компания'
        verbose_name = 'Компании'
        ordering = ['licenses']


class SubCategory(models.Model):
    category = models.ForeignKey(Info, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=25, unique=True, verbose_name='Название')
    certificate = models.ImageField(verbose_name='Сертификат')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Сертификат'
        verbose_name = 'Сертификат'
        ordering = ['name']


