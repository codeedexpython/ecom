from django.db import models

# Create your models here.
class FavoriteStore(models.Model):
    store_id=models.AutoField(primary_key=True)
    store_image=models.ImageField(upload_to='images/')
    store_name=models.CharField(max_length=500)
    rate=models.IntegerField()

    class Meta:
        db_table = "store_table"



