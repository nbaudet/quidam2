from django.contrib import admin
from django.contrib.admin import SimpleListFilter, ModelAdmin

from .models import Category, CategoryDescription, Article, ArticleTranslation


class ArticleFilter(SimpleListFilter):
    title = 'test'
    parameter_name = 'autre test'

    def lookups(self, request, model_admin):
        articles = set([a.article for a in model_admin.model.objects.all()])
        articles.add()
        return [(a.id, a.name) for a in articles]
        # You can also use hardcoded model name like "Country" instead of
        # "model_admin.model" if this is not direct foreign key filter

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(article__id__exact=self.value())
        else:
            return queryset


class ArticleAdmin(ModelAdmin):
    list_filter = (ArticleFilter,)

# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryDescription)
admin.site.register(Article, ArticleFilter)
admin.site.register(ArticleTranslation)