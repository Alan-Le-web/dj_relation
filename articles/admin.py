from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Scope, Article, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        tag_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
               tag_count +=1
        if tag_count !=1:
            raise ValidationError('Должен быть только один основной тег!')




class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]