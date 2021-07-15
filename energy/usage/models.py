from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.TextField(null=False, blank=False)
    address = models.TextField(unique=True)
    meter_number = models.TextField(unique=True)

    def __str__(self):
        return f'{self.meter_number}, {self.name}'


class Rate(models.Model):
    name = models.TextField(unique=True, null=False, blank=False)
    price_gbp_per_kwh = models.DecimalField(decimal_places=5, max_digits=10, null=False, blank=False)

    def __str__(self):
        return self.name


class CustomerReading(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='customerreading')
    rate = models.ForeignKey(Rate, on_delete=models.PROTECT, related_name='customerreading')

    # could have value & energy unit id (foreign key) if not always in kWh
    kwh_reading = models.PositiveIntegerField(null=False, blank=False)

    # would probably be date = models.DateTimeField() irl
    number = models.PositiveSmallIntegerField(null=False, blank=False)

    class Meta:
        unique_together = ('customer', 'rate', 'number')

    def consumption(self):
        prev = CustomerReading.objects.filter(customer=self.customer, rate=self.rate, number=self.number - 1)
        if prev.count() == 1:
            return ((self.kwh_reading - prev[0].kwh_reading)*self.rate.price_gbp_per_kwh)
        return None

    def previous_reading(self):
        prev = CustomerReading.objects.filter(customer=self.customer, rate=self.rate, number=self.number - 1)
        if prev.count() == 1:
            return prev[0].kwh_reading
        return None

    def __str__(self):
        return f'{self.customer}, {self.rate}, #{self.number}: {self.kwh_reading}'


class File(models.Model):
    xlsx = models.FileField(verbose_name='File')