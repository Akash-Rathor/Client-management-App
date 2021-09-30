from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class new_customer(TimeStampMixin):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    age=models.DateField()
    Address = models.CharField(max_length=500)
    phone = models.CharField(max_length=12)
    email=models.EmailField(max_length=40)

    def age_now(self):
        import datetime
        return int((datetime.date.today() - self.age).days / 365.25)
