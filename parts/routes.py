from rest_framework.routers import DefaultRouter
from parts.core.views import *
from parts.requests.views import *

router = DefaultRouter()

router.register("users", AuthUserViewSet, basename="authuser")
router.register("part_requests", PartRequestViewSet, basename="partrequest")
router.register("decision", DecisionViewSet, basename="decision")
