from django.db import models
from django.utils import timezone
# Create your models here.

class ItemType(models.Model):
    name = models.CharField(max_length=200, primary_key=True, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    
    name = models.CharField(max_length=150, null=False, blank=False)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE, null=True, blank=True)
    purchase_cost = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.name + '  ' + str(self.date.day) + '/' + str(self.date.month) + '/' + str(self.date.year)
   

class Rental(models.Model):
    FREQUENCY = [
        ('M', 'mensuel'),
        ('A', 'annuel'),
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, blank=False)
    frequency = models.CharField(max_length=1, choices=FREQUENCY, default='A')
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    start_date = models.DateTimeField(default=timezone.now)
    bill = models.FileField(upload_to='purchase/bills', null=True, blank=True)

    def __str__(self):
        return self.item.name

    def save(self):
        new = False
        
        try:
            Purchase.objects.get(item=self.item)
        except:
            new = True

        if new:
            new_purchase = Purchase.objects.create(
                item=self.item,
                amount=self.amount,
                due_date=self.start_date
            )
            new_purchase.save()

        return super().save()


class Purchase(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    due_date = models.DateTimeField()
    payment_date = models.DateTimeField(null=True, blank=True)
    bill = models.FileField(upload_to='purchase/bills', null=True, blank=True)

    def __str__(self):
        return self.item.name

