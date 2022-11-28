from django.db import models

# Create your models here.
class Contact(models.Model):
    sno     = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=255)
    email   = models.EmailField(max_length=255)
    phone   = models.CharField(max_length=15)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    # Meta class specify the table name
    class Meta:
        db_table = "contact"

    def __str__(self):
        return self.name
    