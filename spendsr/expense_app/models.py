from django.db import models

# Create your models here.
class categorymaster(models.Model):
    id = models.BigAutoField(primary_key= True)
    category_name = models.CharField(max_length=50)
    is_valid = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}  {self.category_name}"

class expensemaster(models.Model):
    id =models.BigAutoField(primary_key=True)
    category_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    is_valid = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} {self.category_id} {self.amount}"

