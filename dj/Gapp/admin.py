from django.contrib import admin
from Gapp import models

admin.site.register(models.VIP)
admin.site.register(models.User)
admin.site.register(models.Manager)
admin.site.register(models.ShopInformation)
admin.site.register(models.VIPInformation)
admin.site.register(models.SearchHistory)
#admin.site.register(models.Visitor)
admin.site.register(models.Adress)

class MesAdmin(admin.ModelAdmin):
    list_display=('id','Shop_Name','Mes_Percent','Mes_Stars','Mes_Suspicious')
admin.site.register(models.Mes,MesAdmin)