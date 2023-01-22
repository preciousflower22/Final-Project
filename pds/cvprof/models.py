from django.db import models

# Create your models here.


class CVModel(models.Model):
    fullname = models.CharField(max_length=255)
    position = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    contact = models.IntegerField()
    skill = models.CharField(max_length=50,null=True)
    firstskills = models.CharField(max_length=50,null=True)
    secondskills = models.CharField(max_length=50,null=True)
    thirdkills = models.CharField(max_length=50,null=True)
    fourthskills =models.CharField(max_length=50, null=True)
    language =models.CharField(max_length=50, null=True)
    firstlanguage =models.CharField(max_length=50, null=True)
    secondlanguage =models.CharField(max_length=50, null=True)
    thirdlanguage =models.CharField(max_length=50, null=True)
    work_experience = models.CharField(max_length=500,null=True)
    firstwork_experience = models.CharField(max_length=500,null=True)
    workexper_descrip = models.TextField(null=True)
    second_experience = models.CharField(max_length=500,null=True)
    third_experience = models.CharField(max_length=500,null=True)
    education = models.CharField(max_length=250, null=True)
    primaryschool = models.CharField(max_length=250, null=True)
    secondaryschool = models.CharField(max_length=250, null=True)
    tertiaryschool = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.fullname
