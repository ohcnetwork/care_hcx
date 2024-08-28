from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from care.utils.queryset.facility import get_facility_queryset
from hcx.api.serializers.claim import ClaimSerializer
from hcx.models.base import Use, Outcome
from hcx.models.claim import Claim
from hcx.utils.queryset.claim import get_claims


class PolicyFilter(filters.FilterSet):
    consultation = filters.UUIDFilter(field_name="consultation__external_id")
    policy = filters.UUIDFilter(field_name="policy__external_id")
    use = filters.ChoiceFilter(field_name="use", choices=Use.choices)
    outcome = filters.ChoiceFilter(field_name="outcome", choices=Outcome.choices)


class ClaimViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = Claim.objects.all().select_related(
        "policy", "created_by", "last_modified_by"
    )
    permission_classes = (IsAuthenticated,)
    serializer_class = ClaimSerializer
    lookup_field = "external_id"
    search_fields = ["consultation", "policy"]
    filter_backends = (
        filters.DjangoFilterBackend,
        drf_filters.SearchFilter,
        drf_filters.OrderingFilter,
    )
    filterset_class = PolicyFilter
    ordering_fields = [
        "id",
        "created_date",
        "modified_date",
    ]

    def get_queryset(self):
        return get_claims(self.request.user, self.queryset)
