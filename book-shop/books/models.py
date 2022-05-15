from django.db import models
from django.contrib.auth import get_user_model 

class Book(models.Model):
    title = models.CharField(max_length= 64)
    author = models.CharField(max_length=64)
    publishing_year = models.IntegerField(default= 1950 ,null= True , blank= True)
    rating = models.IntegerField(default= 0)
    review = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title