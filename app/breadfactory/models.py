from django.db import models


class Orders(models.Model):
    code_orders = models.IntegerField(blank=False, null=False)
    number = models.IntegerField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    summary = models.IntegerField(blank=False, null=False)
    code_items = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.code_orders

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


class Items(models.Model):
    code_items = models.IntegerField(blank=False, null=False)
    name = models.CharField(blank=False, null=False, max_length=100)
    weight = models.IntegerField(blank=False, null=False)
    code_factor = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изделия'
        verbose_name_plural = 'Изделия'


class Factors(models.Model):
    num_factors = models.IntegerField(blank=False, null=False)
    type_item = models.CharField(max_length=100, blank=False, null=False)
    sort_muka = models.CharField(max_length=100, blank=False, null=False)
    sum_of_workers = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.num_factors

    class Meta:
        verbose_name = 'Производственные цеха'
        verbose_name_plural = 'Производственные цеха'


class Production(models.Model):
    code_items = models.IntegerField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    is_ready = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return self.code_items

    class Meta:
        verbose_name = 'Цеха'
        verbose_name_plural = 'Цеха'


class Orderers(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказчики'
        verbose_name_plural = 'Заказчики'