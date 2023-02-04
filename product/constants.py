from django.utils.translation import gettext_lazy as _


class ProductCategoryType:
    NONE_TYPE = "none"
    SHIRT = "shirt"
    SPORTS = "sports"
    # HANDSET = "handset"
    # TABLET = "tablet"

    CHOICES = (
        (NONE_TYPE, _("User defined")),
        (SHIRT, _("Shirt")),
        (SPORTS, _("Sports")),
        # (HANDSET, _("Handset")),
        # (TABLET, _("Tablet")),
    )


class LABELS:
    PRIMARY = "primary"
    SECONDARY = "secondary"
    DANGER = "danger"

    CHOICES = (
        (PRIMARY, _("primary")),
        (SECONDARY, _("secondary")),
        (DANGER, _("danger")),
    )