from django.db import models
from parts.core.models import MetaModel


class PartRequest(MetaModel):
    nomen = models.CharField(max_length=200)
    part_num = models.CharField(max_length=100)
    cos = models.PositiveIntegerField(default=2)
    qty = models.PositiveIntegerField(default=1)
    uoi = models.CharField(max_length=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    requested_by = models.ForeignKey("core.AuthUser", on_delete=models.CASCADE)


class Decision(MetaModel):
    actioned_by = models.ForeignKey("core.AuthUser", on_delete=models.CASCADE)
    request = models.ForeignKey(PartRequest, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=30,
        choices=[
            ("approved", "Approved"),
            ("rejected", "Rejected"),
            ("pending", "Pending"),
            ("need_more", "Need More Info"),
        ],
        default="pending",
    )

    class Meta:
        unique_together = ("actioned_by", "request")
