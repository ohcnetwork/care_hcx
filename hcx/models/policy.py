from django.db import models

from care.facility.models.patient import PatientRegistration
from hcx.models.base import (
    Outcome, Status, Priority, Purpose
)
from care.users.models import User
from care.utils.models.base import BaseModel


class Policy(BaseModel):
    patient = models.ForeignKey(PatientRegistration, on_delete=models.CASCADE)

    subscriber_id = models.TextField(null=True, blank=True)
    policy_id = models.TextField(null=True, blank=True)

    insurer_id = models.TextField(null=True, blank=True)
    insurer_name = models.TextField(null=True, blank=True)

    status = models.CharField(
        choices=Status.choices, max_length=20, default=Status.ACTIVE.value
    )
    priority = models.CharField(
        choices=Priority.choices, max_length=20, default=Priority.NORMAL.value
    )
    purpose = models.CharField(
        choices=Purpose.choices, max_length=20, default=Purpose.BENEFITS.value
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
        related_name="policy_last_modified_by",
    )
