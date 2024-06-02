from django.db import models

from django.db.models.fields import EmailField

from django.contrib.auth.models import AbstractUser



# Create your models here.



class User(AbstractUser):


    user_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=30)

    email = models.EmailField(unique=True, max_length=100)

    password = models.CharField(max_length=30)

    username = None


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']


    def __str__(self):

        return f"Name:{ self.first_name, self.last_name } Email:{ self.email}"



class CreditCard(models.Model):


    card_id = models.AutoField(primary_key=True)

    owner_user = models.ForeignKey(User, on_delete=models.CASCADE)

    card_name = models.CharField(max_length=30)

    card_bank = models.CharField(max_length=30)

    closing_date = models.DateField()

    due_date = models.DateField()


    REQUIRED_FIELDS = ['owner_user', 'card_name', 'card_bank', 'closing_date', 'due_date']


    def __str__(self):

        return f"Card { self.card_name } from { self.owner_user }"


class Revenue(models.Model):

    revenue_id = models.AutoField(primary_key=True)

    owner_user = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.CharField(max_length=30)

    value = models.DecimalField(max_digits=10, decimal_places=2)

    revenue_date = models.DateField()

    isRecurrent = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['owner_user', 'description', 'value', 'revenue_date', 'isRecurrent']

    def __str__(self):
        return f"Revenue { self.description } from { self.owner_user }"

class Bills(models.Model):

    bill_id = models.AutoField(primary_key=True)

    owner_user = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.CharField(max_length=30)

    value = models.DecimalField(max_digits=10, decimal_places=2)

    bill_date = models.DateField()

    isRecurrent = models.BooleanField(default=False)

    hasInstallments = models.BooleanField(default=False)

    payment_method = models.CharField(
        max_length=30,
        choices=[
            ('credit_card', 'Credit Card'),
            ('debit_card', 'Debit Card'),
            ('pix', 'Pix'),
            ('cash', 'Cash'),
            ('others', 'Others')
        ],)

    REQUIRED_FIELDS = ['owner_user', 'description', 'value', 'bill_date', 'isRecurrent']

    def __str__(self):
        return f"Bill { self.description } from { self.owner_user }"