from django.urls import include, path
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from posts.views import UserViewSet, PostViewSet, CommentViewSet


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    """Mixin class for nested routing"""


router = NestedDefaultRouter()

authors_router = router.register("owners", UserViewSet)
authors_router.register(
    "posts",
    PostViewSet,
    basename="owners-posts",
    parents_query_lookups=["owner"])


urlpatterns = [
    path('', include(router.urls)),
]
