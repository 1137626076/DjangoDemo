from django.db import models

# Create your models here.

class user(models.Model):
    id = models.AutoField(primary_key=True, null=False, max_length=11, unique=True)
    username = models.CharField(max_length=255)
    login_name = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    professional_class = models.CharField(max_length=225, null=False)

    class Meta:
        db_table = 'IOmember'


    def __str__(self):
        return self.id, self.username, self.login_name

    def get_password(self):
        return self.password