from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse

from common.models import ProductBaseModel
from common.constants import ZERO
from ..constants import LABELS

from .category import ProductCategory


class Product(ProductBaseModel):
    name = models.CharField(
        max_length=256,
        help_text=_("Name of product.")
    )
    # TODO: We will handle the pricing differently
    price = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        default=ZERO,
        verbose_name=_("Price"),
        help_text=_("Price per product. This is the unit price of the product."),
    )
    discount_price = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        default=ZERO,
        verbose_name=_("Discount price"),
        null=True,
        help_text=_("Discount Price per product."),
    )
    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        help_text=_("Related Category"),
        related_name="categories",
    )
    label = models.CharField(choices=LABELS.CHOICES, default=LABELS.PRIMARY, max_length=32)
    in_stock = models.PositiveIntegerField(
        default=0,
        help_text=_("Amount of available products.")
    )
    short_description = models.TextField(
        help_text=_("Short summary, can be used in search results."),
        blank=True,
        default="",
    )
    long_description = models.TextField(
        help_text=_("Long Description"),
        blank=True,
        default=""
    )
    image = models.ImageField(
        upload_to="product_images/%Y/%m/%d/",
        max_length=500,
        verbose_name=_("Image"),
        help_text=_("Product base image."),
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(
                fields=['code', 'name', 'product_category', 'in_stock']
            ),
        ]

    def __str__(self):
        return f"{self.code}-{self.name}"

    def get_absolute_url(self):
        # TODO: its is using now for product details page, we will fix it later
        return reverse("store:product-details", kwargs={"pk": self.pk})

    def get_product_image(self):
        return self.image.url