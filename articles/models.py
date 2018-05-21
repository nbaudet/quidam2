from django.db import models
from quidam2.settings import LANGUAGES
from django.utils.translation import ugettext_lazy as _

INACTIVE = 0
ACTIVE = 1
STATUS = (
    (INACTIVE, _('Inactive')),
    (ACTIVE, _('Active')),
)


class Category(models.Model):
    """
    Manages the categories for each article
    """
    def upload_path(self, filename):
        return 'category/{}'.format(filename)

    name = models.CharField(unique=True, max_length=80)
    picture = models.ImageField(null=True, upload_to=upload_path)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CategoryDescription(models.Model):
    """
    Stores the category description in each language
    """
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    language = models.CharField(unique=True, max_length=2, choices=LANGUAGES)
    description = models.TextField(null=True)

    def __str__(self):
        return '{} - {}'.format(self.category, self.language)


class Article(models.Model):
    """
    Manages the articles of the shop, and links its descriptions in different languages and product picture
    """
    def upload_path(self, filename):
        return 'article/{}'.format(filename)

    name = models.CharField(unique=True, max_length=80)
    picture = models.ImageField(null=True, upload_to=upload_path)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    active = models.IntegerField(default=1, choices=STATUS)

    def __str__(self):
        return '{} ({})'.format(self.name, self.category)


class ArticleTranslation(models.Model):
    """
    Manages the different fields of an article in a certain language
    """
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    language = models.CharField(unique=True, max_length=2, choices=LANGUAGES)

    def __str__(self):
        return '{} {}'.format(self.article, self.language)
