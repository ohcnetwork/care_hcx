from hcx.models.policy import Policy
from care.utils.queryset.facility import get_facility_queryset


def get_policies(user, queryset=Policy.objects.all()):    
    allowed_facilities = get_facility_queryset(user)
    queryset = queryset.filter(
        policy__patient__facility__id__in=allowed_facilities
    )

    return queryset