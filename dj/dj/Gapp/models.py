import json
from django.db import models


class User(models.Model):
    UserIP = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Create Day")

class VIP(models.Model):
    VIP_Account = models.CharField(max_length=200)
    VIP_Password = models.CharField(max_length=200)
    VIP_Email = models.EmailField(max_length=200, blank=True)
    VIP_Name = models.CharField(max_length=200)
    VIP_PaySituation = models.BooleanField()

# class Visitor(models.Model):
#     Visitor_Account = models.CharField(max_length=200)
#     Visitor_Password = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("Create Day")

class Manager(models.Model):
    Manager_Account = models.CharField(max_length=200, default='')
    Manager_Password = models.CharField(max_length=200, default='')
    Manager_Name = models.CharField(max_length=200, default='')


class VIPInformation(models.Model):
    VIPInformation_Collect = models.CharField(max_length=200, default='')
    VIPInformation_Feadback = models.CharField(max_length=200, default='')

class SearchHistory(models.Model):
    SearchHistory_SearchShop = models.CharField(max_length=200, default='')
    SearchHistory_SearchTime = models.CharField(max_length=200, default='')




class Mes(models.Model):
    # def Message(request):
    #     A = '雙月'
    #     all_reviews = ['隊伍永遠那麼長，可是值得等候！食物太美味了而且價錢實惠！員工服務超棒超專業，美中不足的是位子有點少。強推蠔和剝皮椒雞湯。餐點：5服務：5氣氛：3' ,
    #                     '餐點十分好吃，有一定的水準；店員也很親切，現場吃需要等待時間，外帶建議可以先線上點餐後前往領取，非常方便。' ,
    #                     '雖然位置不多，但是店員都很親切的招待也於等待時送上茶水。這次吃了經典蛤蜊雞腿跟愛恨椒芝麵。湯鮮甜，麵有彈性不軟爛，但也不會太乾。實至名歸。建議的餐點蛤蜊燉雞湯 愛恨椒芝麵'
    #                     ]   
    #     Mes_Percent = "70%"
    #     Mes_Stars = "****"
    #     Mes_Suspicious = [
    #         "值得等候","位置不多","超棒超專業","餐點：5服務：5氣氛：3"
    #     ]

    #     unit = Mes.objects.create(Shop_Name = A, Mes_Percent = Mes_Percent, Mes_Stars=Mes_Stars, Mes_Suspicious=Mes_Suspicious) 
    #     unit.save()  #寫入資料庫



        # ShopName = models.ForeignKey('ShopInformation', on_delete=models.CASCADE, default='')
        Shop_Name = models.CharField(max_length=500, default='')
        Mes_Percent = models.CharField(max_length=100)
        Mes_Stars = models.CharField(max_length=100, default='')
        Mes_Suspicious = models.CharField(max_length=500, default='')

class Adress(models.Model):
    longitude = models.CharField(max_length=500, default='')
    latitude = models.CharField(max_length=500, default='')
    AdressName = models.CharField(max_length=500, default='')

class ShopInformation(models.Model):
    ShopInformation_Name = models.CharField(max_length=500, default='')

        


    
        
    
    


    
