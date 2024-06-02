from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import *


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

class billsCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=30)

    REQUIRED_FIELDS = ['category']

    def __str__(self):
        return f"Category { self.category }"

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

    CREDIT = 'CRD'
    DEBIT = 'DBT'
    CASH = 'CSH'
    PIX = 'PIX'
    BOLETO = 'BLT'
    OTHER = 'OTH'

    PAYMENT_METHOD_CHOICES = {
        CREDIT: 'Credit Card',
        DEBIT: 'Debit Card',
        CASH: 'Cash',
        PIX: 'Pix',
        BOLETO: 'Boleto',
        OTHER: 'Other',
    }

    bill_id = models.AutoField(primary_key=True)

    owner_user = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.CharField(max_length=30)

    value = models.DecimalField(max_digits=10, decimal_places=2)

    bill_date = models.DateField()

    is_recurrent = models.BooleanField(default=False)

    payment_method = models.CharField(
        max_length=3,
        choices=PAYMENT_METHOD_CHOICES,
        default=CREDIT,
        )

    has_installments = models.BooleanField(default=False)

    category = models.ForeignKey(billsCategory, null=True, on_delete=models.SET_NULL)

    REQUIRED_FIELDS = ['owner_user', 'description', 'value', 'bill_date', 'is_recurrent', 'has_installments', 'payment_method']

    def __str__(self):
        return f"Bill { self.description } from { self.owner_user }"

class Installments(models.Model):
    
        installment_id = models.AutoField(primary_key=True)

        bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)

        card_id = models.ForeignKey(CreditCard, on_delete=models.CASCADE)

        installment_number = models.IntegerField()
    
        installments_total_number = models.IntegerField()
    
        installment_date = models.DateField()

        is_payed = models.BooleanField(default=False)
    
        REQUIRED_FIELDS = ['bill_id', 'card_id', 'installment_number', 'installments_total_number', 'installment_date', 'is_payed']
    
        def __str__(self):
            return f"Installment { self.installment_number } of { installments_total_number } from { self.bill_id }"

