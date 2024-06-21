from django.db import models

class Message(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "msges_table"