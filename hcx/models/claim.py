from django.db import models
from django.db.models import JSONField

from care.facility.models.patient import PatientConsultation
from hcx.models.base import (
    ClaimType, Outcome, Priority, Status, Use
)
from hcx.models.json_schema.claim import ITEMS
from hcx.models.policy import Policy
from care.users.models import User
from care.utils.models.base import BaseModel
from care.utils.models.validators import JSONFieldSchemaValidator


class Claim(BaseModel):
    consultation = models.ForeignKey(PatientConsultation, on_delete=models.CASCADE)
    policy = models.ForeignKey(
        Policy, on_delete=models.CASCADE
    )

    items = JSONField(default=list, validators=[JSONFieldSchemaValidator(ITEMS)])
    total_claim_amount = models.FloatField(blank=True, null=True)
    total_amount_approved = models.FloatField(blank=True, null=True)

    use = models.CharField(
        choices=Use.choices, max_length=20, default=Use.CLAIM.value
    )
    status = models.CharField(
        choices=Status.choices, max_length=20, default=Status.ACTIVE.value
    )
    priority = models.CharField(
        choices=Priority.choices, max_length=20, default=Priority.NORMAL.value
    )
    type = models.CharField(
        choices=ClaimType.choices, max_length=20, default=ClaimType.INSTITUTIONAL.value
    )

    outcome = models.CharField(
        choices=Outcome.choices, max_length=20, default=None, blank=True, null=True
    )
    error_text = models.TextField(null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    last_modified_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="claim_last_modified_by",
    )
