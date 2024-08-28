from django.db import models
from typing import Optional

class BaseTextChoices(models.TextChoices):
    """
    Base class for all text choices.
    """

    @classmethod
    def get(cls, item: str) -> Optional["BaseTextChoices"]:
        """
        Enables accessing enum by label, name or value.
        """
        for member in cls:
            if member.label == item or member.name == item or member.value == item:
                return member
        return None

# http://hl7.org/fhir/fm-status
class Status(BaseTextChoices):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    DRAFT = "draft"
    ENTERED_IN_ERROR = "entered-in-error"


# http://terminology.hl7.org/CodeSystem/processpriority
class Priority(BaseTextChoices):
    IMMEDIATE = "stat"
    NORMAL = "normal"
    DEFERRED = "deferred"


# http://hl7.org/fhir/eligibilityrequest-purpose
class Purpose(BaseTextChoices):
    AUTH_REQUIREMENTS = "auth-requirements"
    BENEFITS = "benefits"
    DISCOVERY = "discovery"
    VALIDATION = "validation"


# http://hl7.org/fhir/remittance-outcome
class Outcome(BaseTextChoices):
    QUEUED = "queued"
    COMPLETE = "complete"
    ERROR = "error"
    PARTIAL_PROCESSING = "partial"

# http://hl7.org/fhir/claim-use
class Use(BaseTextChoices):
    CLAIM = "claim"
    PRE_AUTHORIZATION = "preauthorization"
    PRE_DETERMINATION = "predetermination"

# https://terminology.hl7.org/CodeSystem-claim-type
class ClaimType(BaseTextChoices):
    INSTITUTIONAL = "institutional"
    ORAL = "oral"
    PHARMACY = "pharmacy"
    PROFESSIONAL = "professional"
    VISION = "vision"
