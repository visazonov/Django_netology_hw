from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Tag, Scope

# Register your models here.

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        exists = []
        all_marks = []
        for form in self.forms:
            exists.append(form.cleaned_data.get('tag'))
            all_marks.append(form.cleaned_data.get('is_main'))
        available = all_marks.count(True)
        if exists == list(set(exists)):
            pass
        else:
            raise ValidationError('Нельзя добавлять одинаковые теги')
        if available == 0:
            raise ValidationError('Укажите основной тег!')
        if available > 1:
            raise ValidationError('Основной тег должен быть только один!')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

