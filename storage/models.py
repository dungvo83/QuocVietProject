from django.db import models
import uuid
from django.urls import reverse, reverse_lazy

from django import template
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage(location='/media/items')


class Category(models.Model):

    # Field
    objects = models.Manager()
    name = models.CharField(help_text='Enter the name of the Category', max_length=200)
    description = models.TextField(help_text='Enter the brief description of the Category')

    # class Meta
    class Meta:
        ordering = ['name']

    # Method
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('category_delete', kwargs={"pk": self.pk})

    def get_items(self):
        return Item.objects.filter(category=self)[:3]


class Item(models.Model):

    # Field
    objects = models.Manager()
    name = models.CharField(help_text='Enter the name of the Item', max_length=200)
    image = models.ImageField(upload_to='items', blank=True, null=True)
    #models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    description = models.TextField(
        help_text='Enter the brief description of the Item', blank=True, null=True)
    category = models.ForeignKey("storage.Category", on_delete=models.SET_NULL, null=True)

    # class Meta
    class Meta:
        ordering = ['name']

    # Method
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("item_delete", kwargs={"pk": self.pk})


class ItemAction(models.Model):

    # Field
    objects = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for each action')
    date = models.DateField(help_text='Enter the date of the action', blank=True, null=True)
    price = models.FloatField(help_text='Enter the price of the item', default=0)
    quantity = models.BigIntegerField(help_text='Enter the number of item', default=0)
    item = models.ForeignKey("storage.Item", on_delete=models.SET_NULL, null=True)

    IO_STATUS = (
        ('i', 'Input'),
        ('o', 'Output'),
    )

    status = models.CharField(
        choices=IO_STATUS,
        help_text='',
        max_length=1,
        default='o',
        blank=True,
    )

    # Meta
    class Meta:
        ordering = ['-date']

    # Method
    def __str__(self):
        return f'{self.id} ({self.item.name}) - {self.status}'

    def get_absolute_url(self):
        return reverse("itemaction_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('itemaction_delete', kwargs={'pk': self.pk})

    def get_total(self):
        return self.price * self.quantity
