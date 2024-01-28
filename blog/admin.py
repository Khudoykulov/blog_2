from django.contrib import admin
from .models import AboutMe, Partners, Subblog, Blog, Tags, Categories


class PartnersInline(admin.TabularInline):
    model = Partners
    extra = 0


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'tel', 'birth', 'address')
    list_display_links = ('id', 'name', 'email', 'message', 'tel', 'birth', 'address')
    search_fields = ('name', 'email', 'tel', 'birth',)
    readonly_fields = ('created_date',)
    date_hierarchy = 'created_date'
    inlines = [PartnersInline]


class SubblogAdminInline(admin.TabularInline):
    model = Subblog
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'category', 'created_date',)
    list_display_links = ('id', 'name', 'category', 'created_date',)
    search_fields = ('name',)
    readonly_fields = ('created_date', 'slug')
    date_hierarchy = 'created_date'
    autocomplete_fields = ('author',)
    filter_horizontal = ('tags',)
    inlines = [SubblogAdminInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)







