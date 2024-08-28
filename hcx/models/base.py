from django.db import models


# http://hl7.org/fhir/fm-status
class Status(models.TextChoices):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    DRAFT = "draft"
    ENTERED_IN_ERROR = "entered-in-error"


# http://terminology.hl7.org/CodeSystem/processpriority
class Priority(models.TextChoices):
    IMMEDIATE = "stat"
    NORMAL = "normal"
    DEFERRED = "deferred"


# http://hl7.org/fhir/eligibilityrequest-purpose
class Purpose(models.TextChoices):
    AUTH_REQUIREMENTS = "auth-requirements"
    BENEFITS = "benefits"
    DISCOVERY = "discovery"
    VALIDATION = "validation"


# http://hl7.org/fhir/remittance-outcome
class Outcome(models.TextChoices):
    QUEUED = "queued"
    COMPLETE = "complete"
    ERROR = "error"
    PARTIAL_PROCESSING = "partial"

# http://hl7.org/fhir/claim-use
class Use(models.TextChoices):
    CLAIM = "claim"
    PRE_AUTHORIZATION = "preauthorization"
    PRE_DETERMINATION = "predetermination"

# https://terminology.hl7.org/CodeSystem-claim-type
class ClaimType(models.TextChoices):
    INSTITUTIONAL = "institutional"
    ORAL = "oral"
    PHARMACY = "pharmacy"
    PROFESSIONAL = "professional"
    VISION = "vision"
