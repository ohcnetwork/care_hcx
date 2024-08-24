from hcx.api.viewsets.claim import ClaimViewSet
from hcx.api.viewsets.communication import CommunicationViewSet
from hcx.api.viewsets.gateway import HcxGatewayViewSet
from hcx.api.viewsets.policy import PolicyViewSet

from hcx.api.viewsets.listener import (
    ClaimOnSubmitView,
    CommunicationRequestView,
    CoverageElibilityOnCheckView,
    PreAuthOnSubmitView,
)


from django.shortcuts import HttpResponse
from django.urls import path
from rest_framework.routers import DefaultRouter


def healthy(request):
    return HttpResponse("Hello from care hcx")


router = DefaultRouter()

router.register("policy", PolicyViewSet, basename="hcx-policy")
router.register("claim", ClaimViewSet, basename="hcx-claim")
router.register("communication", CommunicationViewSet, basename="hcx-communication")
router.register("", HcxGatewayViewSet, basename="hcx-gateway")

urlpatterns = [
    path("health", healthy),
    path(
        "coverageeligibility/on_check",
        CoverageElibilityOnCheckView.as_view(),
        name="hcx_coverage_eligibility_on_check",
    ),
    path(
        "preauth/on_submit",
        PreAuthOnSubmitView.as_view(),
        name="hcx_pre_auth_on_submit",
    ),
    path(
        "claim/on_submit",
        ClaimOnSubmitView.as_view(),
        name="hcx_claim_on_submit",
    ),
    path(
        "communication/request",
        CommunicationRequestView.as_view(),
        name="hcx_communication_on_request",
    ),
] + router.urls