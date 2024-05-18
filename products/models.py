from django.db import models
from users.models import Merchants, Users, Admins


class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='Books/Authors', null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Authors'
        verbose_name = 'Author'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Genre(models.Model):
    title = models.CharField(max_length=128)
    cr_by = models.ForeignKey(Admins, on_delete=models.DO_NOTHING, related_name='added_by')
    cr_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Genres'
        verbose_name = 'Genre'

    def __str__(self):
        return self.title


class Languages(models.Model):
    lang_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=64)
    cr_by = models.ForeignKey(Admins, on_delete=models.DO_NOTHING, related_name='lang_added_by')
    cr_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Languages'
        verbose_name = 'Language'

    def __str__(self):
        return self.language


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Authors)
    genre = models.ManyToManyField(Genre)
    book_publisher = models.CharField(max_length=128)
    year_of_publishing = models.DateField(null=True, blank=True)
    count_of_page = models.PositiveIntegerField()
    book_size = models.CharField(max_length=64)
    cover_type = models.CharField(max_length=64)
    book_weight = models.PositiveIntegerField()
    age_limit = models.CharField(max_length=16)
    library = models.ManyToManyField(Merchants)
    languages = models.ManyToManyField(Languages)
    preview = models.ImageField(upload_to='books', null=True, blank=True)
    price = models.PositiveIntegerField()
    discount = models.IntegerField(default=0)
    added_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Books'
        verbose_name = 'Book'

    def __str__(self):
        return self.title



