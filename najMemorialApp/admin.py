
from django.contrib import admin
from najMemorialApp.models import Contact, frontImg,Gallary,Commentq,verify_bot
# Register your models here.
admin.site.register(Gallary)
admin.site.register(frontImg)
admin.site.register(Contact)
admin.site.register(Commentq)
admin.site.register(verify_bot)