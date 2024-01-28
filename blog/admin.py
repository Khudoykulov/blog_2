from django.contrib import admin
from .models import AboutMe, Partners


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





