from django.db import models

class CarouselSlide(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel_images/')
    link = models.URLField(blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        db_table='carousel_table'



