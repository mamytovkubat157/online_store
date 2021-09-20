from django.db import models


class Category(models.Model):
    """ Category of products """

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорияи'

    name = models.CharField('Название категории', max_length=250)

    def __str__(self):
        return self.name


class Property(models.Model):
    """ Properties of products, tec-info """

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойство'

    fio = models.CharField('Свойство', max_length=200, db_index=True, unique=True)
    foto = models.ImageField('фото', blank=True, null=True, upload_to='')
    email = models.EmailField(max_length=200)
    # adres = models.CharField('max_length=255')

    # product = models.ManyToManyField('product', related_name='product')

    def __str__(self):
        return self.fio


class Product(models.Model):
    """ Products in catalogue """

    class Meta:
        verbose_name = 'Название продукта'
        verbose_name_plural = 'Название продукта'

    name = models.CharField('Название продукта', max_length=250, db_index=True)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    time_created = models.DateTimeField('Дата и время создания товара', auto_now_add=True)
    time_updated = models.DateTimeField('Дата и время последнего изменения', auto_now_add=True)
    title_img = models.ImageField('Изображение', upload_to='Shop/Article/static/images')
    # discount = models.CharField('скидка')
    categories = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        null=True,
        related_name='categorys'
    )

    def __str__(self):
        return self.price


class Basket(models.Model):
    class Meta:
        verbose_name = 'карзинка'
        verbose_name_plural = 'карзинки'

    date = models.CharField(max_length=200, db_index=True)
    title_img = models.ImageField('Изображение', upload_to='products/')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    Product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True
    )
    Property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.price


class Mycard(models.Model):
    class Meta:
        verbose_name = 'VISA'
        verbose_name_plural = 'VISA'

    card = models.CharField(max_length=20)
    product = models.ManyToManyField('product', related_name='product')
    property = models.ManyToManyField('property', related_name='product')

    def __str__(self):
        return self.card
