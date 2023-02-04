from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import ProductBaseModel
from product.constants import ProductCategoryType


class ProductCategory(ProductBaseModel):
    name = models.CharField(
        max_length=128,
        help_text=_("Name of the Product Type."),
        unique=True
    )
    description = models.TextField(
        help_text=_("Description of the Product Type."),
        blank=True, default="",

    )
    category = models.CharField(
        max_length=32,
        choices=ProductCategoryType.CHOICES,
        default=ProductCategoryType.NONE_TYPE,
    )

    class Meta:
        ordering = ['-id', 'name', 'category']
        indexes = [
            models.Index(
                fields=['name', 'is_available', 'category', ]
            ),
        ]

    def __str__(self):
        return self.name
