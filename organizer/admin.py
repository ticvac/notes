from django.contrib import admin
from .models import Composer, Piece, Sheet, SetList, SetListRelation, Tag

# Register your models here.
admin.site.register(Composer)
admin.site.register(Piece)
admin.site.register(Sheet)
admin.site.register(SetList)
admin.site.register(SetListRelation)
admin.site.register(Tag)