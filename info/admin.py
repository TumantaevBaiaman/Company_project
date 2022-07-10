from django.contrib import admin
from .models import Category, SubCategory, Info, Licenses, Forma, Comment

admin.site.register(Info)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Licenses)
admin.site.register(Forma)
admin.site.register(Comment)

# Register your models here.
