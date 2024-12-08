from django.contrib import admin
from .models import Post,Comment,Contact
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)



admin.site.site_header = 'Varanasi Blog | ADMIN PANEL'
admin.site.site_title = 'Varanasi Blog | BLOGGING WEBSITE'
admin.site.index_title= 'VKJournal Site Administration'
