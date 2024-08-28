from hcx.models.communication import Communication
from care.utils.queryset.facility import get_facility_queryset


def get_communications(user, queryset=Communication.objects.all()):
    allowed_facilities = get_facility_queryset(user)
    queryset = queryset.filter(
        claim__policy__patient__facility__id__in=allowed_facilities
    )

    return queryset