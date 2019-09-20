from django.contrib import admin
from testapp.models import hydjobs,blorejobs,chennaijobs,punejobs

# Register your models here.
class hydjobsadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(hydjobs,hydjobsadmin)

class blorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(blorejobs,blorejobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
