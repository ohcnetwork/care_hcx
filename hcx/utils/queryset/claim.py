from hcx.models.claim import Claim
from care.utils.queryset.facility import get_facility_queryset


def get_claims(user, queryset=Claim.objects.all()):
    allowed_facilities = get_facility_queryset(user)
    queryset = queryset.filter(
        consultation__facility__id__in=allowed_facilities
    )

    return queryset