from rest_framework.serializers import (
    CharField,
    FloatField,
    JSONField,
    ModelSerializer,
    UUIDField,
)

from care.facility.api.serializers.patient_consultation import (
    PatientConsultationSerializer,
)
from care.facility.models.patient_consultation import PatientConsultation
from hcx.api.serializers.policy import PolicySerializer
from hcx.models.base import (
    ClaimType, Outcome, Priority, Status, Use
)
from hcx.models.claim import Claim
from hcx.models.policy import Policy
from care.users.api.serializers.user import UserBaseMinimumSerializer
from config.serializers import ChoiceField
from care.utils.serializer.external_id_field import ExternalIdSerializerField

TIMESTAMP_FIELDS = (
    "created_date",
    "modified_date",
)


class ClaimSerializer(ModelSerializer):
    id = UUIDField(source="external_id", read_only=True)

    consultation = ExternalIdSerializerField(
        queryset=PatientConsultation.objects.all(), write_only=True, required=True
    )
    consultation_object = PatientConsultationSerializer(
        source="consultation", read_only=True
    )

    policy = ExternalIdSerializerField(
        queryset=Policy.objects.all(), write_only=True, required=True
    )
    policy_object = PolicySerializer(source="policy", read_only=True)

    items = JSONField(required=False)
    total_claim_amount = FloatField(required=False)
    total_amount_approved = FloatField(required=False)

    use = ChoiceField(choices=Use.choices, required=False)
    status = ChoiceField(choices=Status.choices, required=False)
    priority = ChoiceField(choices=Priority.choices, required=False)
    type = ChoiceField(choices=ClaimType.choices, required=False)

    outcome = ChoiceField(choices=Outcome.choices, read_only=True)
    error_text = CharField(read_only=True)

    created_by = UserBaseMinimumSerializer(read_only=True)
    last_modified_by = UserBaseMinimumSerializer(read_only=True)

    class Meta:
        model = Claim
        exclude = ("deleted", "external_id")
        read_only_fields = TIMESTAMP_FIELDS

    def validate(self, attrs):
        if "total_claim_amount" not in attrs and "items" in attrs:
            total_claim_amount = 0.0
            for item in attrs["items"]:
                total_claim_amount += item["price"]

            attrs["total_claim_amount"] = total_claim_amount

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        validated_data["last_modified_by"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.last_modified_by = self.context["request"].user
        return super().update(instance, validated_data)
